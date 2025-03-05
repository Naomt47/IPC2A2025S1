
from EncabezadoFilas import EncabezadoFilas
class Tejido:
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.rejilla = EncabezadoFilas()

    def cargarRejilla(self, rejilla):
        for y in range(self.filas): #5
            #print(rejilla)
            self.rejilla.agregarUltimo(rejilla[y*self.filas], y*self.filas)
            #print("en y", y*self.filas)
            for x in range(1,self.columnas):
                
                self.rejilla.agregarColumna(y*self.filas, rejilla[y*self.filas+x], y*self.filas+x)
                #print("en x", y*self.filas+x)
                        
        self.rejilla.graficar2()
        print("se grafico con exito")

