# importamos random para generar los numeros aleatorios
import random

# definimos la funcion y su parametro
def separar_par_impar(n):
    # generamos N números aleatorios entre 50 y 100
    arreglo_original = [random.randint(50, 100) for _ in range(n)]

    # declaramos las variables 'pares' e 'impares' donde se almacenaran los numeros (pares o impares) en un arreglo
    pares = []
    impares = []
    
    # recorremos el arreglo original para clasificar los números
    for num in arreglo_original:
        if num % 2 == 0:
            pares.append(num)     # Si el residuo es 0, es PAR
        else:
            impares.append(num)   # De lo contrario, es IMPAR
            
    return arreglo_original, pares, impares

# establecemos una variable para indicar la cantidad de números deseados
cantidad = 10  # Número de elementos N

# declaramos las variables para almacenar el arreglo original y los demás arreglos organizados
original, lista_pares, lista_impares = separar_par_impar(cantidad)

# imprimimos los resultados: original - pares- impares
print(f"Arreglo original ({cantidad} elementos): {original}") # (ej:)Arreglo original (10 elementos): [63, 80, 98, 89, 79, 99, 69, 71, 74, 51]
print(f"Arreglo de pares ({len(lista_pares)} elementos): {lista_pares}") # Arreglo de pares (3 elementos): [80, 98, 74]
print(f"Arreglo de impares ({len(lista_impares)} elementos): {lista_impares}") # Arreglo de impares (7 elementos): [63, 89, 79, 99, 69, 71, 51]