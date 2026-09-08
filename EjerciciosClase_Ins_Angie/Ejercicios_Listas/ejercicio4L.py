precios = [15000, 8000, 22000, 5000]

total = 0

for precio in precios:
    total += precio

promedio = total / len(precios)

print("El total es de:",total,"/","El promedio es de:",promedio)