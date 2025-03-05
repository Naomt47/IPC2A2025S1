from proteina import Celda

class NodoColumna(Celda):
    def __init__(self, proteina, indice=-1, estado=False):
        #Dato
        super().__init__(proteina, indice, estado)
        
        #Apuntador
        self.siguiente = None