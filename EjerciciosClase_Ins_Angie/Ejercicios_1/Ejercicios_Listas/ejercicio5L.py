edades = [15, 22, 17, 30, 16, 25]

mayores = []
menores = []

for edad in edades:
    if edad >= 18:
        mayores.append(edad)
    else:
        menores.append(edad)

print("Mayores de edad", mayores)
print("Menores de edad", menores)