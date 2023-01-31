class Producto:

    def __init__(self, codigo, nombre, precio):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__precio = precio

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, valor):
        self.__codigo = valor

    @property
    def nombre(self):
        return self.__nombre

    @codigo.setter
    def nombre(self, valor):
        self.__nombre = valor

    @property
    def precio(self):
        return self.__precio

    @codigo.setter
    def precio(self, valor):
        self.__precio = valor

    def calcular_total(self, unidades):
        return self.__precio * unidades

    def __str__(self):
        return "Codigo: " + str(self.__codigo) + ", Nombre: " + self.__nombre + ", Precio: " + "€" + str(self.__precio)\
               + "€"
class Pedido:

    def __init__(self, productos, cantidades):
        self.__productos = productos
        self.__cantidades = cantidades

    def total_pedido(self):
        total = 0

        for (p, c) in zip(self.__productos, self.__cantidades):
            total = total + p.calcular_total(c)

        return total

    def mostrar_pedido(self):
        for (p, c) in zip(self.__productos, self.__cantidades):
            print("Producto:", p.nombre,  ",cantidad: " + str(c))

p1 = Producto(1, "Cerveza", 2)
p2 = Producto(2, "Cubata", 5)
p3 = Producto(3, "Pincho", 4)

print(p1)
print(p2)
print(p3)

productos = [p1, p2, p3]
cantidades = [2, 2, 2]

pedido = Pedido(productos, cantidades)

print("Total pedido: " + str(pedido.total_pedido()))

pedido.mostrar_pedido()







