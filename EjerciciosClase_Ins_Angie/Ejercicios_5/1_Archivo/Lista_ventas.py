# Creamos ventas.txt con un valor por línea
ventas = [45000, 120000, 8000, 300000]

# Guardamos y abrimos ventas.txt en modo escritura
with open("ventas.txt", "w") as f:
    for venta in ventas:
        f.write(f"{venta}\n")

# Leemos el archivo, además de convertir cada línea a número y calcular el total
# Definimos el valor inicial
total = 0

#Abrimos ventas.txt en modio lectura
with open("ventas.txt", "r") as f:
    for linea in f:
        # mediante float convertimos el texto a numero antes de acomularlo en la variable total
        total += float(linea.strip())

print(f"El total de ventas es: {total}")