class Banco: 
    def __init__(self, nombre, direccion, antiguedad, sucursales, clientes):
        self.nombre = nombre 
        self.direccion = direccion 
        self.antiguedad = antiguedad
        self.sucursales = sucursales
        self.clientes = clientes 

    def promedio(self):
        suma = 0
        for cliente in self.clientes:
            suma += cliente.saldo
        return int(suma/len(self.clientes))
