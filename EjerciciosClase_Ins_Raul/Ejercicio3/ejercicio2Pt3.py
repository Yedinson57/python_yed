# elaboramos el algoritmo definiendo la funcion
def busqueda_secuencial(arreglo, valor_buscado):
    # recorremos el arreglo elemento por elemento usando su índice
    for i in range(len(arreglo)):
        if arreglo[i] == valor_buscado:
            return i  # retorna el índice (posición) donde se encontró el valor
    
    return -1  # retorna -1 si el valor no está en el arreglo

# --- asignamos valores y el valor a buscar ---
numeros = [15, 42, 8, 23, 4, 16]
valor = 23

# definimos una variable para saber la posicion del numero ingresado y su valor
posicion = busqueda_secuencial(numeros, valor)

# mediante un condicional imprimimos el resultado dependiendo de si el valor ingresado se encuentra o no
if posicion != -1:
    print(f"El valor {valor} se encuentra en la posición (índice): {posicion}")
else:
    print(f"El valor {valor} no se encuentra en el arreglo.")