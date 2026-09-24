# Creamos una clase carrito de compras con una lista en la que se puedan agregar productos y un metodo total que sume el carrito
class CarritoCompras:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, nombre, precio):
        self.productos.append({"nombre": nombre, "precio": precio})

    def total(self):
        return sum(producto["precio"] for producto in self.productos)

carrito = CarritoCompras()
carrito.agregar_producto("Camiseta", 35000)
carrito.agregar_producto("Zapatos", 120000)

print("Total del carrito:", carrito.total())  # 155000