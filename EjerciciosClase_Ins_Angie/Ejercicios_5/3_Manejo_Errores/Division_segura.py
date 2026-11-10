def dividir_seguro(a, b):
    try:
        return a / b
    # Pyhton lanza una excepcion ZeroDivisionError al intentar dividir cualquier numero entre cero
    except ZeroDivisionError:
        # El bloque except captura este escenario específico, emite la advertencia y retorna none de forma segura
        print("Aviso: No se puede dividir entre cero.")
        return None

# Pruebas
print(dividir_seguro(10, 2))  # Devuelve 5.0
print(dividir_seguro(5, 0))   # Muestra aviso y devuelve None