# definimos la funcion para contar los elementos del diccionario y su parametro
def contar_elementos_diccionario(lista):
    # declaramos el diccionario, clave - valor
    conteo = {'positivos': 0, 'negativos': 0, 'ceros': 0}

    # declaramos un ciclo for para que recorra la lista
    for num in lista:
        # establecemos las condiciones y si cumple alguna de ellas sumamos 1 al conteo
        if num > 0:
            conteo['positivos'] += 1
        elif num < 0:
            conteo['negativos'] += 1
        else:
            conteo['ceros'] += 1
            
    return conteo

# asignamos valores
numeros = [-5, 12, 0, -3, 8, 0, 4, -1]
# usamos la funcion para contar y los valores (numeros)
resultado = contar_elementos_diccionario(numeros)

# imprimimos el resultado
print(resultado)
# {'positivos': 3, 'negativos': 3, 'ceros': 2}