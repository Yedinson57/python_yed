# Al envolverlo en un bloque try/except, evitamos que la aplicación colapse y en su lugar mostramos solo un mensaje
try:
    with open("no_existe.txt", "r", encoding="utf-8") as f:
        contenido = f.read()
# Si se intenta abrir un archivo que no existe se dispara la excepción FileNotFoundError
except FileNotFoundError:
    print("El archivo no existe. Revisa el nombre o la carpeta.")