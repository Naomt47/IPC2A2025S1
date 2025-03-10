
from xml.dom import minidom # Importar librería minidom
from ListaBanco import ListaBanco

newList = ListaBanco()

def LeerArchivoMD(rutaArchivo):
    doc = minidom.parse(rutaArchivo) # Parsear el archivo XML
    root = doc.documentElement # Obtener la raíz del archivo XML

    bancos = root.getElementsByTagName('Banco') # Obtener todos los nodos Banco
    contadorBancos = 0
    for banco in bancos:
        nombreBanco = banco.getAttribute('nombre')
        direccionBanco = banco.getAttribute('direccion')
        ant = int(banco.getElementsByTagName('Antiguedad')[0].firstChild.data)
        sucursales = int(banco.getElementsByTagName('sucursales')[0].firstChild.data)

        #bancoObj = Banco(nombreBanco, direccionBanco, ant, sucursales, []) #Recordatorio: En el proyecto no es permitido utilizar listas nativas como listaBancos
        #Agregamos un nuevo banco a la lista
        newList.agregarUltimo(contadorBancos, nombreBanco, direccionBanco, ant, sucursales)

        clientes = banco.getElementsByTagName('Cliente')
        for cliente in clientes:
            nombreCliente = cliente.getElementsByTagName('Nombre')[0].firstChild.data
            cuiCliente = int(cliente.getElementsByTagName('CUI')[0].firstChild.data)
            saldoCliente = float(cliente.getElementsByTagName('Saldo')[0].firstChild.data)
            edadCliente = int(cliente.getElementsByTagName('edad')[0].firstChild.data)

            #clienteObj = Cliente(nombreCliente, cuiCliente, saldoCliente, edadCliente)
            #bancoObj.clientes.append(clienteObj)
            #AL BANCO LE AGREGAMOS UN NUEVO CLIENTE
            newList.agregarCliente(nombreBanco, nombreCliente, cuiCliente, saldoCliente, edadCliente)

        #listaBancos.append(bancoObj) #Recordatorio: En el proyecto no es permitido utilizar listas nativas como listaBancos
        contadorBancos += 1


    print('Datos leídos con éxito con minidom')

    newList.recorrer()
    #newList.graficar()
    """for b in listaBancos: #Recordatorio: En el proyecto no es permitido utilizar listas nativas
        print('\n', b)
        for c in b.clientes:
            print('\t >>', c.nombre, " | ", c.cui," | ", c.saldo," | ", c.edad)"""
    

LeerArchivoMD("ejemplo.xml")
newList.eliminarCliente("Banrural",7884299560101) #Pepito
newList.graficar()

