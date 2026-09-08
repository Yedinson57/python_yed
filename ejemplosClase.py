# tupla - estructura de datos que permite almacenar varios elementos ordenados en una sola variable
# Tupla con tres valores, cada uno de un tipo diferente.
t = (1, 'a', 3.5)

print(t)

print("---")

# listas
animales=["Gato","Perro","Loro"]
animales.append("Pez")
animales.remove("Perro")
animales[1]="Aguila"
animales[0]="Leon"

print(animales)

print("---")

temperaturas=[22,18,30,25,26,20]
temperaturas.append(20.5)
temperaturas[4]=16
temperaturas.remove(18)

promedio =  sum(temperaturas) / len(temperaturas)
maximo = max(temperaturas)
minimo = min(temperaturas)

print(temperaturas)
print("Promedio:",promedio)
print("Max",maximo)
print("Min",minimo)

print("---")

#diccionarios
persona = {"nombre":"Ana", "edad":18}
persona["edad"] = 22
persona["ciudad"] = "Popayan"

print(persona)

print("---")

Estudiantes = [{
    "nombre:":"Camila",
    "curso:":"Python Basico",
    "nota:":4.5,
    "aprobado:":True
},
{
    "nombre:":"David",
    "curso:":"Python Basico",
    "nota:":3,
    "aprobado:":True
},
{
    "nombre:":"Samuel",
    "curso:":"Python Basico",
    "nota:":4,
    "aprobado:":True 
}]

Estudiantes[1]["nota:"]=5

for Estudiantes in Estudiantes:
    for clave,valor in Estudiantes.items(): print(clave,valor)