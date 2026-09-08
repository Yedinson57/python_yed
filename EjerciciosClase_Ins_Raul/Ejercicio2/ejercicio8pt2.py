#asignamos valor
poten = 0

# hacemos uso de un ciclo for para saber las potencias de 4 en un rango de 1 a 30
for i in range(1,31):
    # realizamos la operacion
    poten = 4**i
    #imprimimos el resultado
    print(f"4 elevado a la {i} es igual a {poten}")