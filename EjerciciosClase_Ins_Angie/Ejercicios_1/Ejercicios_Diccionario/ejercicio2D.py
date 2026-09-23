notas = {"Matematicas":8.5, "Inglés":7.0, "Programación":9.2}

total = 0
cantidad = 0

for nota in notas.values():
    total += nota
    cantidad += 1

promedio = total / cantidad
print("El promedio es:", promedio)