# definimos la funcion para insertar y ordenar los numeros
def insertar_y_ordenar(lista, nuevo_valor):
    lista.append(nuevo_valor)  # Agrega al final
    lista.sort()               # Ordena la lista internamente 

# asignamos valores
numeros = [2, 5, 8, 12, 16]

# el nuevo numero que vamos a insertar
nuevo = 10

# hacemos uso de la función 
insertar_y_ordenar(numeros, nuevo)

# imrpimimos el resultado
print(numeros)  # [2, 5, 8, 10, 12, 16]