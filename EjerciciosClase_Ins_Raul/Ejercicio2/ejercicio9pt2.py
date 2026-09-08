# asignamos valor
suma = 0

# hacemos uso de un ciclo for para sumar solo los primeros numeros pares entre un rango de 1 a 30
for i in range(1, 31):
    # establecemos el condicional if y laoperacion de modulo para saber los numeros pares
    if i % 2 == 0:
        # realizamos la operacion
        suma += i
    # imrpimimos el resultado
    print(f"la suma es {suma}")

