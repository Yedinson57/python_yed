# Calcular que medalla merece un estudiante
def cal_medalla(nota):
    if nota > 4.5:
        return "Oro"
    elif nota >= 4.0:
        return "Plata"
    elif nota >= 3.8:
        return "Bronce"
    else:
        return "Sin medalla"
        
print(cal_medalla(5))
print(cal_medalla(4))
print(cal_medalla(3.9))
print(cal_medalla(1))