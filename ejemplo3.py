# tupla - estructura de datos que permite almacenar varios elementos ordenados en una sola variable
# Tupla con tres valores, cada uno de un tipo diferente.
t = (1, 'a', 3.5)

print(t)

# Los elementos de una tupla son accesibles a través delíndice que ocupan en la misma.
t = (1, 'a', 3.5)

print(t[1]) # a

# Anidamiento de tuplas
tp = (1, ('a', 3), 5.6)

print(tp) # (1, ('a', 3), 5.6)

# concatenacion de tuplas
t1 = (1, 'a', 5.6)
t2 = (2, 'b')
t3 = t1 + t2

print(t3) # (1, 'a', 5.6, 2, 'b)

# * sirve para crear una tupla donde se repiten
tpo = (1, 'a', 5.6)

print(tpo*2) # (1, 'a', 5.6, 1, 'a', 5.6)(1, 'a', 5.6, 1, 'a', 5.6)

# metodo index() - indice de la posicion que ocupa en la tupla
ti = ('a', 'c', 'r')

print(ti.index('c')) # 1

# metodo count() - obtiene el numero de ocurrencias de un numero (lo que repite)
tc= (1, 3, 1, 5, 1,)

print(tc.count(1)) # 3

# una tupla es un objeto iterable; es decir con un ciclo for se pueden recorrer todos sus elementos
tit = (1,('a', 3), 5.6)
for ele in tit:
    print(ele)
# 1
# ('a', 3)
# 5.6

print('--- separador listas ---')

# Lista - se usan corchetes []
lista = []
li = [2, 'a', 4]

print(li)

# A diferencia de las tuplas, los elementos de las listas pueden ser reemplazados accediendo a traves del indice que ocupan en la lista
li = [2,'a', 4]
li[1] = 'b'

print(li) #[2, 'b', 4]

# comprobr si un determinado valor existe en una lista a tarves de un opeador in (True - si, False - No)
li = [2, 'a', 4]

print('a' in li) # True

# La función tuple() devuelve un tupla al recibir como argumento una lista
li = [2, 'a', 4]
tup = tuple(li)

print(tup) # (2, 'a', 4)

# Añadir elementos a listas mediante el metodo append() - se añade al final de la lista
li = [2, 'a', 4]
li.append('nuevo')

print(li) # [2, 'a', 4, 'nuevo']

# Al igual que las tuplas, las listas son iterables, se puede recorrer usando bucle (for..)
li = [2, 'a', 4]

for ele in li:
    print(ele)
#2
#a
#4

# metodo insert() sirve para insertar elementos en una lista pero necesitamos el indice y el valor que vamos a insertar
li = [2, 'a', 4]
li.insert(3, 'c')

print(li) # [2, 'a', 4, 'c']

# si el indice ingresado no existe (12) lo pone por defecto en la ultima 
li = [2, 'a', 4]
li.insert(12, 'c')

print(li) # [2, 'a', 4, 'c']

# se puede decidir donde se coloca el valor
li = [2, 'a', 4]
li.insert(0, 'c')

print(li) # ['c', 2, 'a', 4]

# borra el elemento con la funcion del() recibe como argumento el indice
li = [2, 'a', 4]
del(li[1])

print(li) # [2, 4]

# el metodo remove() borra un elemento de una lista a través de su valor
li = [2, 'a', 4]
li.remove('a')

print(li) # [2, 4]

# se puede ordenar listas a traves del metodo sort() o sorted()
lista = [3, 1, 9, 8, 7]

print( sorted(lista) ) # [1, 3, 7, 8, 9]
print( sorted(lista, reverse = True) ) # [9, 8, 7, 3, 1]
print(lista) # [3, 1, 9, 8, 7]

# El metodo sort() ordena la lista pero quedara automáticamente modificada
lista = [3, 1, 9, 8, 7]
lista.sort()

print(lista) # [1, 3, 7, 8, 9]

# si tenemos texto podemos ordenar por oden alfabetico
lis = ['be', 'ab', 'cc', 'aa', 'cb']
lis.sort()

print(lis) # ['aa', 'ab', 'be', 'cb', 'cc']

# ordenacion funcion sorted sin parametro adicional
lis = ['Aa', 'Ab', 'Cc', 'ca']

print(sorted(lis)) # ['Aa', 'Ab', 'Cc', 'ca']

# el parametro key fijara como ordenar los elementos al pasar como argumento un determinado criterio de ordenacion
lis = ['aA', 'Ab', 'Cc', 'ca']

print(sorted(lis, key=str.lower)) # ['aA', 'Ab', 'ca', 'Cc']

# El metodo reverse() ordena la lista al orden inverso pero la modifica
lista = [3, 1, 9, 8, 7]
lista.reverse ()

print(lista) #

print('--- separador matriz ---')

# anidando listas se pueden construir matrices de elementos
matriz = [[1, 2, 3],[4, 5, 6]]

print(matriz[0][1]) # 2

# cambiar un elemento en una matriz
matriz = [[1, 2, 3],[4, 5, 6]]
matriz[0][1] = 33

print(matriz) # [[1, 33, 3], [4, 5, 6]]

print('--- separador diccionario ---')

# Declaracion de un diccionario con 3 valores - almacena informacion en pares de clave y valor
diccionario = {'a': 1, 'b': 2, 'c':3}

print(diccionario) # {'a': 1, 'b': 2, 'c': 3}

# alternativamente se puede usar dict() para crear un diccionario
diccionario = dict(a=1, b=2, c=3)

print(diccionario) # {'a': 1, 'b': 2, 'c': 3}

# en diccionarios se usa clave para cceder al valor de cada elemento
diccionario = {'a':1, 'b':2, 'c':3}

print(diccionario['c']) #3

# para modificar un valor en un diccionario de datos
diccionario = {'a':1, 'b':2, 'c':3}
diccionario['b'] = 5

print(diccionario) # {'a': 1, 'b': 5, 'c': 3}

# si la clave no existe Python agregara su valor correspondiente
diccionario = {'a':1, 'b':2, 'c':3}
diccionario['d'] = 4

print(diccionario) #{'a': 1, 'b': 2, 'c': 3, 'd': 4}

# metodo keys() -- trae solamente las claves del diccionario -- y de la funcion integrada list() --forma la lista --
diccionario = {'a':1, 'b':2, 'c':3}
lista = list(diccionario.keys())

print(lista) # ['a', 'b', 'c']

# usar values() trae solamente los valores del diccionario
diccionario = {'a':1, 'b':2, 'c':3}
lista = list(diccionario.values())

print(lista) # [1, 2, 3]

# devolver una lista de tuplas, donde cada una de ellas contenga dos elementos, la clave y valor del diccionario
diccionario = {'a':1, 'b':2, 'c':3}
lista = list(diccionario.items())

print(lista) # [('a', 1), ('b', 2), ('c', 3)]

# la funcion integrada del() eliminara un valor de un dicionario
diccionario = {'a':1, 'b':2, 'c':3}
del(diccionario['b'])

print(diccionario) # {'a': 1, 'c': 3}

# operador in sirve para comprobar si una clave existe (True or False)
diccionario = {'a':1, 'b':2, 'c':3}

print('x' in diccionario) # False

# funcion integrada sorted() devuelve una lista ordenada de las claves contenidas
diccionario = {'a':1, 'b':2, 'c':3}

print(sorted(diccionario)) # ['a', 'b', 'c']

# metodo items() da acceso tanto a claves como a valores
diccionario = {'a':1, 'b':2, 'c':3}

for k, v in diccionario.items():
    print("clave={0}, valor={1}".format(k, v))

#clave=a, valor=1
#clave=b, valor=2
#clave=c, valor=3

# metodo values( se encarga de devolver los valores)
diccionario = {'a':1, 'b':2, 'c':3}

for v in diccionario.values():
    print("valor={0}".format(v))

# valor=1
# valor=2
# valor=3

# metodo keys() devuelve las claves del diccionario
diccionario = {'a':1, 'b':2, 'c':3}

for k in diccionario.keys():
    print("clave={0}".format(k))

# clave=a
# clave=b
# clave=c
