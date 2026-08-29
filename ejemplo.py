num_negativo = -78
print(num_negativo) # numero negativo

num_complejo = 3.2 + 7j
print(num_complejo) # numero complejo

num_complex = 5j + 3
print(num_complex) # (3+5j)

num_real = 0.5e-7
print(num_real) #5e-08

num_binario = 0b111
print(num_binario) # 7

num_octal = 0o10
print(num_octal) # 8

num_hexa = 0xff
print(num_hexa) # 255

a = 12
b = 5
c = 6

print(a + b) # suma
print(a - b) # resta
print(a * b) # multiplicacion
print(a / b) # division
print(a // b) # redondeo hacia abajo
print(a % b)  # resto
print(a ** b) # potenciacion

resultado = a + b * c # expresion
print(resultado)

valor_absoluto = abs(-47.67) # valor absoluto
print(valor_absoluto)

import math
raiz_cuadrada = math.sqrt(169) # raiz cuadrada
print(raiz_cuadrada)

redondeo = round(42.4) # redondeo al mas cercano
print(redondeo)

cad_multiple = "Hola" "M" "N" # cadena multiple
print(cad_multiple)

cadena = "cadena de texto de ejemplo"
print(len(cadena)) # longitud de la cadena - 26

cad = "xyza"
print(cad.find("y")) # enconrer la posicion de un caracter

cad2 = "Hola mundo"
res = cad2.replace("Hola", "Adios") # reemplazar una cadena por otra
print(res) 

cad3 = " cadena con espacios en blanco "
esp = cad3.strip() # eliminar espacios en blanco al inicio y al final
espi = cad3.lstrip() # eliminar espacios en blanco al inicio
espd = cad3.rstrip() # eliminar espacios en blanco al final

print(esp) # cadena sin espacios al inicio y al final
print(espi) # cadena sin espacios al inicio
print(espd) # cadena sin espacios al final

cad4 = "cadena DE Texto"
may = cad4.upper() # convertir a mayusculas
min = cad4.lower() # convertir a minusculas

print(may) # cadena en mayusculas
print(min) # cadena en minusculas

cad5 = "hola mundo"
print(cad5.capitalize()) # convertir la primera letra a mayuscula

cad6 = " primer valor;segundo;tercer valor"
print(cad6.split(";")) # convertir una cadena en una lista 

cad_concat = "Hola " + "Mundo" # concatenar cadenas
print(cad_concat) # Hola Mundo

cad7 = "mundo"
cad8 = "cadena"
print("Hola" + cad7 + "Otra" + cad8) # concatenar directamente dos variables de tipo cadena
print("Hola {0} Otra {1}".format(cad7, cad8)) # concatenar con format
print("Hola {texto1}, Otra {texto2}".format(texto1=cad7, texto2=cad8)) # concatenar con format y variables nombradas

num = 3
print("Número: "+str(num)) # concatenar con str, texto y numero - Número: 3

print("Hola Mundo" * 4) # concatenar una cadena varias veces

cad9 = "Nueva cadena de texto"
res = "x" in cad9 # buscar un caracter en una cadena
print(res) # True

cad10 = "Cadenas"
print(cad10[2]) # devuelve el tercer caracter

cad11 = "Cadenas"
print(cad11[:3]) # devuelve los tres primeros caracteres - subcadenas

cad12 = "Cadenas"
print(cad12[-2]) # devuelve el penultimo caracter - subcadenas

cad13 = "Cadenas"
print(cad13[3:]) # devuelve los tres ultimos caracteres - subcadenas