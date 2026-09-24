# creamos una clase vehiculo con sus atributos y una funcion para cambiar de estado (que invierta la disponibilidad)
class Vehiculo:
    def __init__(self, placa, conductor, disponible=True):
        self.placa = placa
        self.conductor = conductor
        self.disponible = disponible

    def cambiar_estado(self):
        self.disponible = not self.disponible

taxi = Vehiculo("XYZ123", "Marta", True)
print("Estado inicial (disponible):", taxi.disponible)  # True

taxi.cambiar_estado()
print("Estado tras cambio (disponible):", taxi.disponible)  # False