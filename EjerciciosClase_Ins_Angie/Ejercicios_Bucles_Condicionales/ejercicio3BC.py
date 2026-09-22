# Recorre la lista, determina cuantas veces faltó un estudiante y muestra una alerta si falto mas de 2 veces
asistencia_aprendiz = [1, 1, 0, 1, 0, 0, 1]
falto = 0

for aistencia in asistencia_aprendiz:
    if aistencia == 0:
        falto += 1
    
if falto > 2:
    print("El estudiante ha faltado mas de 2 veces")

print(f"Total de faltas del estudiante: {falto}")
        
    