import os
from Nodo import Nodo

class Pila():
    def __init__(self):
        self.cima = None

    def estaVacia(self):
        return self.cima ==  None
    
    def Apilar(self, codigo, titulo, autor):
        nuevo = Nodo(codigo, titulo, autor)
        if self.estaVacia() == True:
            self.cima = nuevo
        else:
            temp = nuevo
            temp.siguiente = self.cima
            self.cima = temp

    def Desapilar(self):
        if self.estaVacia():
            return None
        
        else: 
            temp = self.cima
            self.cima = self.cima.siguiente
            temp.siguiente = None

        return temp
    


    def graficar(self, name):
        temp = self.cima
        contador = 0
        file = open(name+".dot", "w")
        cadena = "digraph G{ \n"
        cadena += "rankdir=TB\n"
        cadena += "node[ shape = record, style=\"filled\", color=\"black\", fillcolor=\"yellow\"];\n"
        while temp != None:
            #cadena += "Nodo"+str(contador)+"[label=\"" + str(temp.cui)+" | "+ temp.nombre+ " | "+ str(temp.precio) + "\"];\n"
            cadena += f"Nodo{contador}[label = \"{temp.codigo} | {temp.titulo} | {temp.autor}  \"]\n"
            if temp != self.cima:
                #cadena += "Nodo"+str(contador-1)+" -> Nodo"+str(contador)+";\n"
                cadena += f"Nodo{contador-1} -> Nodo{contador};\n"
            temp = temp.siguiente
            contador += 1
        
        if self.estaVacia():
            cadena += f"Nodo[label=\"No hay elementos en la pila\", color = \"white\", fillcolor=\"white\"];"

        cadena += "}"
        file.write(cadena)
        file.close()
        os.system("dot -Tpng "+ name+".dot -o "+name+".png")
        print(f"grafica {name} creada con exito")