# hacemos uso de un ciclo for para saber los numero pares e impares entre un rango de 1 a 10
for i in range(1,11):
    # realizamos la operacion para los numeros pares
    par = i * 2
    # realizamos la operacion para saber los cubos de dichos numeros
    cubo = par ** 3
    # imprimimos el resultado
    print(f"par {par} - cubo {cubo}")
