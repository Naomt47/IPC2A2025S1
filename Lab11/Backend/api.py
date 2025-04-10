from flask import Flask, jsonify, request
from xml.etree import ElementTree as ET

api = Flask(__name__)



@api.route("/")
def main():
    return "Si funciona Wuju!!!!"


#1. Mediante URL

#1.1 Parametros por URL
@api.route("/usuario/saludar/<int:carnet>/<string:nombre>", methods=["GET"])
def saludar(carnet, nombre):
    return jsonify({
        "mensaje": f'Hola {nombre} carnet {carnet}', 
        "status": 200
    }), 200





#1.2 Parametros de consulta
@api.route("/usuario/saludar2", methods=["GET"])
def saludar2():
    carnet = request.args.get("carnet", type=int)
    nombre = request.args.get('nombre', type=str)
    return jsonify({
        "mensaje": f'Hola {nombre} carnet {carnet}', 
        "status": 200
    }), 200


#2. Mediante BODY
usuarios = []
@api.route('/usuario/add', methods=['POST'])
def agregarJson():
    data = request.get_json()

    # Extraer los datos
    nombre = data['nombre']
    carnet = data['carnet']

    # Crear un nuevo usuario
    nuevoUsuario = {'id': len(usuarios) + 1, 'nombre': nombre, 'carnet': carnet}
    usuarios.append(nuevoUsuario)

    return jsonify({
        'mensaje': 'Usuario creado exitosamente',
        'usuario': nuevoUsuario,
        'status': 201
    }), 201

@api.route('/usuario/add2', methods=['POST']) 
def recibiendoXML():   
    # Leer el cuerpo de la solicitud como una cadena de texto
    xml = request.data.decode('utf-8')
    root = ET.fromstring(xml)

    # Extraer los datos
    nombre = root.find('nombre').text
    carnet = root.find('carnet').text

    # Crear un nuevo usuario
    nuevoUsuario = {'id': len(usuarios) + 1, 'nombre': nombre, 'carnet': carnet}
    usuarios.append(nuevoUsuario)
    print(nuevoUsuario)
    return jsonify({
        'mensaje': 'Usuario creado exitosamente',
        'usuario': nuevoUsuario,
        'status': 201
    }), 201

if __name__ == '__main__':
    api.run(debug=True)