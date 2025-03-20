class Nodo():
    def __init__(self, codigo, titulo, autor):
        
        #Dato
        self.codigo = codigo
        self.titulo = titulo
        self.autor  = autor

        #Apuntador
        self.siguiente = None
