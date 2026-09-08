print('ejercicio numero mayor:')
# tupla - numero mayor
T = (12, 5, 20, 8, 17)
mayor = T[0]

for n in T:
    if n > mayor:
        mayor = n

print("El valor mayor es: ", mayor) # El valor mayor es: 20

print('ejercicio suma:')

# lista - suma
lista = [10, 20, 30, 40, 50]
suma = 0

for elemento in lista:
    suma += elemento

print("Suma de los elementos:", suma) #Suma de los elementos: 150

print('ejercicio promedio:')

# diccionario - calcular el promedio
notas = {
    "Ana":8,
    "Luis":5,
    "Marta":9,
    "Pedro":6,
    "Sofia":4
}
#sum = 0
#prom = 0

#for p in notas.values():
#    sum += p
#    prom = sum / len(notas)

#print("El promedio es: ", prom)

promedio = sum(notas.values())/len(notas)

print(promedio)
    

