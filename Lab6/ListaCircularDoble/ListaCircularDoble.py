import os
from Curso import Curso

class ListaCircularDoble:
    def __init__(self):
        self.primero=None
        self.ultimo=None





    def estaVacia(self):
        """if self.primero==None:
            return True
        else:
            return False"""
        return self.primero==None #sel.primero == self.ultimo == None


























    def agregarPrimero(self, codigo, nombre, creditos):
        nuevo=Curso(codigo, nombre, creditos)

        if self.estaVacia():
            self.primero=self.ultimo=nuevo
        else:
            temp=nuevo
            temp.siguiente=self.primero
            self.primero.anterior=temp
            self.primero=temp
        self .__unirNodos()



















    def __unirNodos(self):
        if self.primero!=None:
            self.primero.anterior=self.ultimo
            self.ultimo.siguiente=self.primero






















    def agregarUltimo(self, codigo, nombre, creditos):
        nuevo=Curso(codigo, nombre, creditos)

        if self.estaVacia():
            self.primero=self.ultimo=nuevo
        else:
            temp=self.ultimo
            self.ultimo=temp.siguiente=nuevo
            self.ultimo.anterior=temp
        self .__unirNodos()




















    def eliminarPrimero(self):
        if self.estaVacia():
            print("ERROR: La lista esta vacia")
        elif self.primero==self.ultimo:
            self.primero=self.ultimo=None
        else:
            temp = self.primero
            self.primero=self.primero.siguiente
            temp.siguiente = temp.anterior = None
            
        self .__unirNodos()






















    def eliminarUltimo(self):
        if self.estaVacia():
            print("ERROR: La lista esta vacia")
        elif self.primero==self.ultimo:
            self.primero=self.ultimo=None
        else:
            temp = self.ultimo
            self.ultimo=self.ultimo.anterior
            temp.siguiente = temp.anterior = None
            """temp.anterior = None
            temp.siguiente = None"""
        self .__unirNodos()











    def recorrerInicioFin(self):
        temp=self.primero
        while temp: #temp != None
            print(temp.codigo, temp.nombre, temp.creditos)
            temp=temp.siguiente
            if temp==self.primero:
                break



















    def recorrerFinIncio(self):
        temp=self.ultimo
        while temp:
            print(temp.codigo, temp.nombre, temp.creditos)
            temp=temp.anterior
            if temp==self.ultimo:
                break
















    def buscar(self,codigo):

        temp=self.primero
        while temp:
            if temp.codigo==codigo:
                return temp

            temp=temp.siguiente
            if temp==self.primero:
                return None

    
















    def contendioReporte(self):
        temp=self.primero
        text=""
        text+="rankdir=LR; \n "
        text+="node[shape=egg, style=filled, color=khaki, fontname=\"Century Gothic\"];  graph [fontname = \"Century Gothic\"];\n"
        text+="labelloc=\"t; \"label = \"Cursos\";\n"

        while temp:
            
            text+="x"+str(temp.codigo)+"[dir=both label=\"Codigo ="+str(temp.codigo)+"\\nNombre = "+temp.nombre+" \\nCreditos = "+str(temp.creditos)+ "\"]\n"
            text+="x"+str(temp.codigo)+"-> x"+str(temp.siguiente.codigo) +"\n"
            text+="x"+str(temp.codigo)+"-> x"+str(temp.anterior.codigo) +"\n"
            temp=temp.siguiente
            if temp!=self.primero:
                text+="x"+str(temp.codigo)+"[dir=both label=\"Codigo ="+str(temp.codigo)+"\\nNombre = "+temp.nombre+" \\nCreditos = "+str(temp.creditos)+ "\"]\n"
                #print(text)
            if temp==self.ultimo:
                text+="x"+str(temp.codigo)+ "-> x"+str(temp.siguiente.codigo)+"\n"
                text+="x"+str(temp.codigo)+ "-> x"+str(temp.anterior.codigo)+"\n"
                break
        return text


    def crearReporte(self):
        os.makedirs('Paciente', exist_ok=True)
        contenido="digraph G{\n\n"
        r=open("Paciente/reporte.dot","w")
        contenido+=str(self.contendioReporte())
        contenido+="\n}"
        r.write(contenido)
        r.close()
        print("Grafica Creada")
        os.system("dot -Tpng Paciente/reporte.dot -o Paciente/reporte.png")
        os.system("dot -Tpdf Paciente/reporte.dot -o Paciente/reporte.pdf")