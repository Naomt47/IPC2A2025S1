from ListaCircularDoble import ListaCircularDoble

lista=ListaCircularDoble()

lista.agregarPrimero(771,'IPC 2',4)
lista.agregarPrimero(2009,'Practicas Finales',0)
lista.agregarPrimero(1,'Logica',1)
lista.agregarUltimo(200,'Mate Aplicada 3',5)
lista.agregarUltimo(201,'Mate Aplicada 5',5)

lista.crearReporte()


#Encontrar Logica

'''lista.eliminarUltimo()
lista.eliminarPrimero()'''

print('inicio - final')
lista.recorrerInicioFin()

print('final - inicio')
lista.recorrerFinIncio()

lista.eliminarPrimero()

lista.crearReporte()

"""encontrado = lista.buscar(1)
print("Datos encontrado", encontrado.codigo, encontrado.nombre, encontrado.creditos)


lista.eliminarPrimero()

lista.crearReporte()

print("Datos encontrado", lista.buscar(1))"""

#lista.eliminarUltimo()
#lista.crearReporte()




