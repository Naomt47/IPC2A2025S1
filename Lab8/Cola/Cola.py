import os
from Nodo import Nodo

class Cola():
    def __init__(self):
        self.primero = None 
        self.ultimo = None


    def estaVacia(self):
        return self.primero == self.ultimo == None
    

    def Encolar(self, nombre, cui):
        nuevo = Nodo(cui, nombre)
        if self.estaVacia() == True:
            self.primero = self.ultimo = nuevo
        else:
            self.ultimo.siguiente = nuevo
            self.ultimo = nuevo


    def Desencolar(self):
        if self.estaVacia():
            print("Esta Vacia")
            return None
        else:
            temp = self.primero
            self.primero = self.primero.siguiente
            temp.siguiente = None

        if self.primero == None:
            self.ultimo = None

        return temp
        


    def graficar(self, name):
        temp = self.primero
        contador = 0
        file = open(name+".dot", "w")
        cadena = "digraph G{ \n"
        cadena += "rankdir=LR\n"
        cadena += "node[ shape = record, style=\"filled\", color=\"black\", fillcolor=\"yellow\"];\n"
        while temp != None:
            #cadena += "Nodo"+str(contador)+"[label=\"" + str(temp.cui)+" | "+ temp.nombre+ " | "+ str(temp.precio) + "\"];\n"
            cadena += f"Nodo{contador}[label = \"{temp.cui} | {temp.nombre}  \"]\n"
            if temp != self.primero:
                #cadena += "Nodo"+str(contador-1)+" -> Nodo"+str(contador)+";\n"
                cadena += f"Nodo{contador-1} -> Nodo{contador};\n"
            temp = temp.siguiente
            contador += 1
        
        if self.estaVacia():
            cadena += f"Nodo[label=\"No hay elementos en la cola\", color = \"white\", fillcolor=\"white\"];"

        cadena += "}"
        file.write(cadena)
        file.close()
        os.system("dot -Tpng "+ name+".dot -o "+name+".png")
        print(f"grafica {name} creada con exito")