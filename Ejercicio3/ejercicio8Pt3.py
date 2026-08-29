# asignamos valores a la lista
alturas = [1.70, 1.80, 1.50, 1.45, 2.0]

# Suma total dividida entre la cantidad de elementos
media = sum(alturas) / len(alturas)

# declaramos las variables mayor - menor como contador para las alturas mayores - menores a la media
mayor = 0
menor = 0

# declaramos un ciclo for para recorrer las alturas
for alt in alturas:
    # mediante un condicional establecemos que se sume 1 al respectivo contador
    # si existe una altura mayor o menor a la media
    if alt > media:
        mayor += 1
    elif alt < media:
        menor += 1

# imprimimos los resultados
print('La media de las alturas almacenadas es de:',media) # La media de las alturas almacenadas es de: 1.69
print('El numero de alturas mayores a la media es de:',mayor) # El numero de alturas mayores a la media es de: 3
print('El numero de alturas menores a la media es de:',menor) # El numero de alturas menores a la media es de: 2
