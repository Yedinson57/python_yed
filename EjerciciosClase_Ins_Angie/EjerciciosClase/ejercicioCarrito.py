# Carrito de compras
class carrito_compras:
    def __init__(self):
        self.producto = []
    def agregar_productos (self, nombre, precio):
        self.producto.append({"nombre": nombre, "precio": precio})
    def total (self, destino, descuento = 15):
        total_bruto = sum(p["precio"] for p in self.producto)

        if total_bruto > 300000:
            monto_descuento = (total_bruto * descuento) / 100
            total_final = total_bruto - monto_descuento
            print(f"Aplica descuento del {descuento}%: -${monto_descuento}")
        else:
            total_final = total_bruto
        
        ciudad_normalizada = destino.strip().lower().replace("á", "a")
        
        if ciudad_normalizada == "popayan":
            costo_envio = 0
            print("Envio Gratis")
        else:
            costo_envio = 15000
            print(f"costo envio a {destino}: ${costo_envio}")
        
        total_completo = total_final + costo_envio
        return total_completo
        
carrito = carrito_compras()
carrito.agregar_productos("Camisa", 50000)
carrito.agregar_productos("Gorra para Gato", 50000)
carrito.agregar_productos("Camisa para Gato", 100000)
carrito.agregar_productos("Pantalon", 110000)
print("Valor total $", carrito.total(destino="Cali"))