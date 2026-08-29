# aisgnamos los valores
a = 2
b = 5
c = 3

# establecemos el condicional if para saber el numero mayor entre 3 valores
if a > b and a > c:
    # en caso de que sea "a" imprimimos el siguiente resultado
    print(f"{a} es mayor que {b} y que {c}")
elif b > a and b > c:
    # en caso de que sea "b" imprimimos el siguiente resultado
    print(f"{b} es mayor que {a} y que {c}")
else:
    # en caso de que sea "c" imprimimos el siguiente resultado
    print(f"{c} es mayor que {a} y que {b}")