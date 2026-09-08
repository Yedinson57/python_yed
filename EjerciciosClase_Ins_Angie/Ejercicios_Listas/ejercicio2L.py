asistencias = [1, 0, 1 ,1, 0, 1, 1]
asistio = 0

for asistencia in asistencias:
    if asistencia == 1:
        asistio += 1

print("El estudiante asistió",asistio,"veces")