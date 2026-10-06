# Ejemplo (no evaluable) sobre como funciona las clases y funciones 
import math

class Parqueadero:
    def __init__(self, capacidad_maxima):
        self.capacidad = capacidad_maxima
        # Tarifas por hora según el tipo de vehículo
        self.tarifas = {
            "carro": 3000,
            "moto": 1500,
            "bici": 1000
        }
        # Diccionario para almacenar vehículos dentro: {placa: {"tipo": tipo, "horas": horas}}
        self.vehiculos = {}
        # Historial de salidas: lista de diccionarios con la información de cada cobro
        self.historial = []

    def registrar_ingreso(self, tipo_vehiculo, placa, horas_estimadas=1):
        tipo = tipo_vehiculo.lower()
        placa = placa.upper().strip()

        # Validación 1: Tipo de vehículo válido
        if tipo not in self.tarifas:
            print(f"Error: Tipo de vehículo '{tipo_vehiculo}' no válido. Opciones: carro, moto, bici.")
            return False

        # Validación 2: Capacidad máxima
        if len(self.vehiculos) >= self.capacidad:
            print("Error: Ingreso rechazado. El parqueadero está lleno.")
            return False

        # Validación 3: Formato de placa (exactamente 6 caracteres)
        if len(placa) != 6:
            print(f"Error: La placa '{placa}' no es válida. Debe tener exactamente 6 caracteres.")
            return False

        # Validación 4: El vehículo ya se encuentra dentro
        if placa in self.vehiculos:
            print(f"Error: El vehículo con placa {placa} ya se encuentra ingresado.")
            return False

        # Registrar vehículo
        self.vehiculos[placa] = {
            "tipo": tipo,
            "horas": horas_estimadas
        }
        print(f"Ingreso exitoso: {tipo.capitalize()} con placa {placa}.")
        return True

    def registrar_salida(self, placa):
        placa = placa.upper().strip()

        # Buscar el vehículo
        if placa not in self.vehiculos:
            print(f"Error: El vehículo con placa {placa} no se encuentra en el parqueadero.")
            return None

        # Calcular el cobro
        datos = self.vehiculos.pop(placa)
        tipo = datos["tipo"]
        horas = datos["horas"]
        # Se cobra mínimo 1 hora o las horas redondeadas hacia arriba
        horas_cobro = math.ceil(horas) if horas > 0 else 1
        total_a_pagar = horas_cobro * self.tarifas[tipo]

        # Guardar en el historial
        registro = {
            "placa": placa,
            "tipo": tipo,
            "horas": horas_cobro,
            "cobro": total_a_pagar
        }
        self.historial.append(registro)

        print(f"Salida de {tipo} ({placa}). Total a pagar por {horas_cobro} hora(s): ${total_a_pagar}")
        return total_a_pagar

    def ver_vehiculos_adentro(self):
        print("\n--- Vehículos actualmente en el parqueadero ---")
        if not self.vehiculos:
            print("No hay vehículos adentro.")
            return

        for placa, info in self.vehiculos.items():
            print(f"Placa: {placa} | Tipo: {info['tipo'].capitalize()} | Horas: {info['horas']}")

    def ver_historial(self):
        print("\n--- Historial de Salidas ---")
        if not self.historial:
            print("No hay registros en el historial.")
            return

        for reg in self.historial:
            print(f"Placa: {reg['placa']} | Tipo: {reg['tipo'].capitalize()} | Horas: {reg['horas']} | Cobro: ${reg['cobro']}")

    def total_recaudado(self):
        total = sum(reg["cobro"] for reg in self.historial)
        print(f"\nTotal recaudado: ${total}")
        return total

    def recaudado_por_tipo(self):
        recaudo = {"carro": 0, "moto": 0, "bici": 0}
        for reg in self.historial:
            recaudo[reg["tipo"]] += reg["cobro"]

        print("\n--- Recaudado por Tipo de Vehículo ---")
        for tipo, monto in recaudo.items():
            print(f"{tipo.capitalize()}: ${monto}")
        return recaudo

# ejemplos de uso
if __name__ == "__main__":
    # Instanciamos el parqueadero con capacidad para 3 vehículos
    parqueadero = Parqueadero(capacidad_maxima=3)

    print("--- PRUEBAS DE INGRESO ---")
    parqueadero.registrar_ingreso("carro", "ABC123", horas_estimadas=2.5) # Válido (redondea a 3 hrs = $9000)
    parqueadero.registrar_ingreso("moto", "XYZ987", horas_estimadas=1)   # Válido ($1500)
    parqueadero.registrar_ingreso("bici", "123456", horas_estimadas=4)   # Válido ($4000)

    # Validaciones de error al ingresar
    parqueadero.registrar_ingreso("carro", "LLENO1", horas_estimadas=1)  # Error: Parqueadero lleno
    parqueadero.registrar_ingreso("camión", "CAM123")                   # Error: Tipo no válido (al liberar espacio)
    parqueadero.registrar_ingreso("carro", "123")                       # Error: Placa de longitud distinta a 6

    # Ver vehículos adentro
    parqueadero.ver_vehiculos_adentro()

    print("\n--- PRUEBAS DE SALIDA Y HISTORIAL ---")
    parqueadero.registrar_salida("ABC123")
    parqueadero.registrar_salida("XYZ987")

    # Ver historial y reportes
    parqueadero.ver_historial()
    parqueadero.total_recaudado()
    parqueadero.recaudado_por_tipo()