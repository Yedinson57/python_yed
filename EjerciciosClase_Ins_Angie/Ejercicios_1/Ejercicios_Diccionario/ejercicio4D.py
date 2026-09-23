horario = {
    "Lunes": "Matemáticas",
    "Martes": "Inglés",
    "Miércoles": "Programación"
}

dia = input("Ingrese un día: ")

materia = horario.get(dia, "No hay una materia programada para ese día")

print(materia)