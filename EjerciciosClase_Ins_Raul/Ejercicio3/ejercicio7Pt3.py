# asignamos valores a la lista
temperaturas = [20, 30, 50, 43, 21]

# Suma total dividida entre la cantidad de elementos
media = sum(temperaturas) / len(temperaturas)

# declaramos la variable contador para las temperaturas mayores a la media
contador = 0

# declaramos un ciclo for para recorrer las temperaturas
for temps in temperaturas:

    # mediante un condicional establecemos que se sume 1 al contador
    # si existe una tempertura mayor a la media
    if temps >= media:
        contador += 1

# imprimimos los resultados
print('La media de las temperaturas almacenadas es de:',media)
print('El numero de temperaturas mayores a la media es de:',contador)
