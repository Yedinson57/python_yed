# Creamos una clase con atributos nombre y membresia activa y un metodo para determinar si una persona puede o no entrenar
class Cliente:
    def __init__(self, nombre, membresia_activa=True):
        self.nombre = nombre
        self.membresia_activa = membresia_activa

    def puede_entrenar(self):
        return self.membresia_activa

cliente1 = Cliente("Carlos", True)
cliente2 = Cliente("Ana", False)

print(f"{cliente1.nombre} puede entrenar?: {cliente1.puede_entrenar()}")
print(f"{cliente2.nombre} puede entrenar?: {cliente2.puede_entrenar()}")