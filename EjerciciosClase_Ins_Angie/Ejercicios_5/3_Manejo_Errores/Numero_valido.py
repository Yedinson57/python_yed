while True:
    try:
        # Si el usuario introduce texto en lugar de un número, float() genera un error de tipo ValueError
        numero = float(input("Escribe un número válido: "))
        print(f"Es Correcto. Ingresaste el número: {numero}")
        # break rompe el ciclo en el momento en que se cumple la condición
        break
    # El bloque except interpreta este error, muestra el aviso y el bucle while se repite hasta ingresar un dato correcto
    except ValueError:
        print("Aviso: Eso no es un número válido. Inténtalo de nuevo.")