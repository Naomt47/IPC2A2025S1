from NodoColumna import NodoColumna

class ListaColumnas():
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def estaVacia(self):
        return self.primero  == self.ultimo == None
    
    #Agregar una proteina
    def agregarUltimo(self, proteina, indice):
        nuevo = NodoColumna(proteina, indice)
        if self.estaVacia() == True:
            self.primero = self.ultimo = nuevo
        else:
            temp = nuevo
            self.ultimo.siguiente = temp
            self.ultimo = temp

    def recorrer(self):
        temp = self.primero
        while temp != None:
            print(temp.proteina, temp.indice, temp.estado)
            temp = temp.siguiente

    
    def buscarPorIndice(self, indice):
        temp = self.primero
        while temp !=None:
            if temp.indice == indice:
                return temp
            temp = temp.siguiente
        return None
    

    #SE MODIFICO
    def graficar(self, name):
        temp = self.primero
        contador = 0
        cadena = ""
        while temp != None:
            #cadena += "Nodo"+str(contador)+"[label=\"" + str(temp.cui)+" | "+ temp.nombre+ " | "+ str(temp.precio) + "\"];\n"
            cadena += f"{name}Nodo{contador}[label = \" {temp.proteina} | {temp.indice} \"]\n"
            if temp != self.primero:
                #cadena += "Nodo"+str(contador-1)+" -> Nodo"+str(contador)+";\n"
                cadena += f"{name}Nodo{contador-1} -> {name}Nodo{contador};\n"
            temp = temp.siguiente
            contador += 1
        
        return cadena
    
    def graficar2(self):
        temp = self.primero
        cadena = ""
        while temp != None:
            cadena += f"\t\t<TD border='3' bgcolor='greenyellow' gradientangle='270'>{temp.proteina}</TD>\n"
            temp = temp.siguiente      
        return cadena