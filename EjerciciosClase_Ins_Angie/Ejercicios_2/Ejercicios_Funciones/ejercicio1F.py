# calcular propina con el valor de una cuenta
def calcular_propina(cuenta, porcentaje=10):
    return (cuenta * porcentaje) / 100

print(calcular_propina(10000))