# Importamos json
import json

# Creamos la clase CarritoCompras y le agregamos métodos
class CarritoCompras:
    def __init__(self):
        self.productos = []

    # Definimos el método para agregar producto
    def agregar_producto(self, producto, precio, cantidad):
        self.productos.append({
            "producto": producto, 
            "precio": precio, 
            "cantidad": cantidad
        })

    # Método guardar para que tome los productos internos del carrito y los escriba en un archivo JSON
    def guardar(self, archivo):
        with open(archivo, "w", encoding="utf-8") as f:
            json.dump(self.productos, f, indent=4, ensure_ascii=False)

    def cargar(self, archivo):
        try:
            # Método cargar, abre dicho archivo, lee la información y le asigna el atributo self.productos
            with open(archivo, "r", encoding="utf-8") as f:
                self.productos = json.load(f)
        except FileNotFoundError:
            # Si no se encuentra el archivo se imprime el sigueinte mensaje
            print("El archivo todavía no existe, el carrito está vacío.")

# Prueba con dos carritos distintos
carrito1 = CarritoCompras()
carrito1.agregar_producto("Camisa", 45000, 2)
carrito1.guardar("carrito.json")

carrito2 = CarritoCompras()
print("Antes de cargar:", carrito2.productos)
carrito2.cargar("carrito.json")
print("Después de cargar:", carrito2.productos)