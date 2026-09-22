# Saber si un numero es par
def es_par(numero):
    return numero % 2 == 0

print(es_par(4))
print(es_par(7))

print("- - -")

# calcular el valor total de propina
def cal_propinas(vt_cuenta, por_propina=10):
    return vt_cuenta * (por_propina/100)

print(cal_propinas(18000))
print(cal_propinas(18000, 15))

print("- - -")

# numero de horas y tarifas en un parqueadero
def calcular_pago(horas, tarifa_hora=2000):
    if horas > 8:
        return 10000
    return horas * tarifa_hora

print(calcular_pago(4))
print(calcular_pago(10))

print("- - -")

# Carrito de compras
class carrito_compras:
    def __init__(self):
        self.producto = []
    def agregar_productos (self, nombre, precio):
        self.producto.append({"nombre": nombre, "precio": precio})
    def total (self):
        return sum(p["precio"] for p in self.producto)
    
carrito = carrito_compras()
carrito.agregar_productos("Camisa", 50000)
carrito.agregar_productos("Gorra para Gato", 50000)
carrito.agregar_productos("Pantalon", 110000)
print("Valor total $", carrito.total())