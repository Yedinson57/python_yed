# definimos la lista y sus valores
numeros = [-5, 12, 0, -3, 8, 4, -1]

# filtramos la lista dejando solo los > 0 y calculamos len()
# para saber el numero de elementos positivos en la lista
cantidad_positivos = len([num for num in numeros if num > 0])

# impriminos el resultado
print(cantidad_positivos)  # 3