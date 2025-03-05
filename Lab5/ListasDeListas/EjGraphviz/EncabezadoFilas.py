from NodoFila import NodoFila
import os

class EncabezadoFilas:
    def __init__(self):
        self.primero = None
        self.ultimo = None
    
    #----------------- METODOS PARA MODIFICAR LA LISTA "ENCABEZADO" -----------------

    def estaVacio(self):
        return self.primero == self.ultimo == None
    
    
    
    def agregarUltimo(self, proteina, indice):
        nuevo = NodoFila(proteina, indice)
        if self.estaVacio():
            self.primero = self.ultimo = nuevo
        else:
            nuevo.anterior = self.ultimo
            self.ultimo.siguiente = nuevo
            self.ultimo = nuevo

    def getCelulaEncabezado(self, indice):
        temp = self.primero
        while temp !=None:
            if temp.indice == indice:
                return temp
            temp = temp.siguiente
        return None
    

    def graficar(self):
        temp = self.primero
        contador = 0
        file = open("ListaDoble.dot", "w")
        cadena = "digraph G{ \n"
        cadena += "rankdir=TB\n"
        cadena += "node[ style=\"filled\", color=\"black\", fillcolor=\"yellow\"];\n"
        while temp!=None:
            cadena += 'Nodo'+str(contador)+f"[label=\"{temp.proteina} | {temp.indice}\"];\n"

            #SE OBTIENEN LISTA CLIENTES
            cadena += temp.columnas.graficar(f"Banco{temp.indice}")

            #ENLACE DE NODO BANCO AL PRIMER NODO DE LISTA CLIENTES 
            cadena += 'Nodo'+str(contador)+ '-> '+f"Banco{temp.indice}Nodo0;\n"
            
            if temp != self.primero:
                cadena += 'Nodo'+str(contador-1)+' -> Nodo'+str(contador)+';\n'
                cadena += 'Nodo'+str(contador)+' -> Nodo'+str(contador-1)+';\n'
            temp = temp.siguiente
            contador += 1

        cadena += 'rank = same {'
        for i in range(contador):
            cadena += 'Nodo'+str(i)+" "
        cadena += '}\n'

        file.write(cadena+"}")
        file.close()
        os.system("dot -Tpng ListaDoble.dot -o listaDoble.png")


    def graficar2(self):
        temp = self.primero
        file = open("Rejilla.dot", "w")
        cadena = """digraph G {
label = <<TABLE BORDER="0" CELLSPACING="0">
<TR><TD><B><FONT POINT-SIZE="16">Ejemplo Rejilla</FONT></B></TD></TR>
<TR><TD>
    <TABLE border='2' cellspacing='5' cellpadding='10'>
"""
        while temp!=None:
            cadena += "\t<TR>\n"
            cadena += f"\t\t<TD border='3' bgcolor='greenyellow' gradientangle='270'>{temp.proteina}</TD>\n"

            cadena += temp.columnas.graficar2()
            cadena += "\t</TR>\n"
            temp = temp.siguiente
        cadena +=  "\t</TABLE>"
        cadena += """</TD></TR>
    </TABLE>>;
}"""
        file.write(cadena)
        file.close()
        os.system("dot -Tpng Rejilla.dot -o Rejilla.png")


    #------------------- NUEVOS METODOS(PARA MANEJAR LAS LISTAS DE CADA NODO) -------------------
    def buscarPorIndice(self, indice): #puede ser por id o por cualquier campo que quieran
        temp = self.primero
        while temp !=None:
            if temp.indice == indice:
                return temp
            encontrado = temp.columnas.buscarPorIndice(indice)
            if encontrado != None:
                return encontrado
            temp = temp.siguiente
        return None
    
    

    def agregarColumna(self, posEncabezado, proteina, indice):
        encabezadoFila = self.getCelulaEncabezado(posEncabezado)

        if encabezadoFila != None:
            encabezadoFila.columnas.agregarUltimo(proteina, indice)
        else:
            print(f"No existe el Nodo {encabezadoFila}")
    
    
