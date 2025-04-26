from django.shortcuts import render
import requests
from .forms import FileForm

endpoint = 'http://localhost:4000/'
# Create your views here.
#Esta es una vista de ejemplo, pero puedes agregar las que necesites
def index(request):
    return render(request, 'index.html')

def carga(request):
    return render(request, 'carga.html')

#los contextos son las expresiones que se muestran en los templates
contexto = {
    'contenido_archivo':None,
    'binario_xml':None, 
}


def cargarXML(request):
    try:
        if request.method == 'POST':
      #obtenemos el formulario
            form = FileForm(request.POST, request.FILES)  
            #verificamos si es valido
            if form.is_valid():
                #obtenemos el archivo
                archivo = request.FILES['file']  #file es el label que estamos obteniendo (el nombre que se coloco en id,for,name y en el form)
                #leemos el archivo
                contenido = archivo.read()
                #decodificamos el archivo a utf-8
                contenido_xml = contenido.decode('utf-8')
                #guardamos el contenido en el contexto
                contexto['contenido_archivo'] = contenido_xml
                contexto['binario_xml'] = contenido
                return render(request, 'carga.html', contexto) #le mando el contexto

    except:
        return render(request, 'carga.html', contexto)
    

def procesarXML(request):
    try:
        if request.method == 'POST':
            #obtenemos el archivo
            archivo = contexto['binario_xml']
            if archivo is None:
                return render(request, 'carga.html')
            #enviamos el archivo al servidor 
            ##request con s es para conectarnos con el backend
            response = requests.post(endpoint + 'venta/cargar', data=archivo) #/venta/cargar
            #obtenemos la respuesta en formato json
            respuesta = response.json()
            #guardamos la respuesta en el contexto
            print(respuesta['mensaje'])
            #limpiamos el contexto
            contexto['contenido_archivo'] = None
            contexto['binario_xml'] = None
            return render(request, 'carga.html', contexto)
    except:
        return render(request, 'carga.html', contexto)