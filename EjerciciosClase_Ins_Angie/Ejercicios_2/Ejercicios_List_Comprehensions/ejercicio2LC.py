# usamos una comprehension para convertir las temperaturas a Fahrenheit.
temperaturas = [18, 22, 25, 19, 30]

fahrenheit = [(temp * 9/5) + 32 for temp in temperaturas]
print(fahrenheit)  # [64.4, 71.6, 77.0, 66.2, 86.0]