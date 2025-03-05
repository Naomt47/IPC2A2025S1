import xml.etree.ElementTree as ET
from Tejido import Tejido
def cargarTejido():
    tree = ET.parse("archivo1.xml")
    raiz = tree.getroot()
    for experimento in raiz:
        tejido = experimento.find('tejido')
        filas = int(tejido.attrib['filas'])
        columnas = int(tejido.attrib['columnas'])
        
        rejilla = tejido.find('rejilla')    
        rejilla = rejilla.text.replace("\n", " ").split()
        
        nuevoTejido = Tejido(filas, columnas)
        nuevoTejido.cargarRejilla(rejilla)

cargarTejido()