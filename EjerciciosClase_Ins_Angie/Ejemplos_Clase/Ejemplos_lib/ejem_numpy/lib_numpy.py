import numpy as np

print("-- numeros y operaciones--")

numeros = np.array([10,20,30,40,50])
print(numeros)
print(numeros + 2)
print(numeros * 2)
print(numeros / 10)

print("-- notas --")

# import numpy as np

notas = np.array([[3.5, 4.0, 2.2, 5.0],[4.4, 5.0, 3.0, 3.0],[5.0, 3.8, 4.6, 4.0]])

print(notas.mean(axis = 1)) # axis, prom, 1 o 0 para diagonal o vertical
print(notas.shape) # conocer la dimension o tamaño de la estructura de datos
print(notas[0]) # ver fila y posición
print(notas[:,0]) # ver columna y posicion
print(notas.max()) # maximo
print(notas.min()) # minimo

print("-- calificaciones --")

# import numpy as np

calificaciones = np.array([
    [8.5, 7.9, 9.0], # Carlos
    [6.0, 7.5, 8.0], # Ana
])

print(calificaciones.shape) # (2,3)
print(calificaciones[0]) # fila de Carlos
print(calificaciones[:, 0]) # columna 1