from proteina import Celda
from ListaColumnas import ListaColumnas

class NodoFila(Celda):
    def __init__(self, proteina, indice=-1, estado=False):
        #Dato
        super().__init__(proteina, indice, estado)
        

        #Apuntador
        self.columnas = ListaColumnas()

        self.anterior = None
        self.siguiente = None