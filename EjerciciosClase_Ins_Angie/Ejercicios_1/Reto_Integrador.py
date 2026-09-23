# Lista de diccionarios con los estudiantes
estudiantes = [
    {"nombre": "Alex", "nota": 9.0},
    {"nombre": "Joshman", "nota": 5.5},
    {"nombre": "Luis", "nota": 7.0}
]

# Variable para acumular las notas
total = 0

# Recorremos la lista de estudiantes
for estudiante in estudiantes:
    nombre = estudiante["nombre"]
    nota = estudiante["nota"]

    # Sumamos la nota al total
    total += nota

    # Verificamos si aprobó o reprobó
    if nota >= 6.0:
        print(nombre, "- Aprobado")
    else:
        print(nombre, "- Reprobado")

# Calculamos el promedio general
promedio = total / len(estudiantes)

print("Promedio general del curso:", round(promedio, 2))