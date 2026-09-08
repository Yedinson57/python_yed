# definimos la funcion para saber los numeros pares e impares
def sum_par_impar(lista):
    # declaramos el diccionario, clave - valor
    resultado = {'pares': 0, 'impares': 0}

    # hacemos uso de un ciclo for para recorrer la lista
    for num in lista:

        # mediante un condicional tomaremos los numeros pares e impares independientemente
        if num % 2 != 0:
            resultado['impares'] += num
        else:
            resultado['pares'] += num

    return resultado

# asignamos valores
numeros = [10, 23, 37, 48, 52]

# traemos el resultado de la suma independiente de los numeros (par - impar)
res = sum_par_impar(numeros)

# imprimimos el resultado
print('la suma de los números es',res) # {'pares': 110, 'impares': 60}
