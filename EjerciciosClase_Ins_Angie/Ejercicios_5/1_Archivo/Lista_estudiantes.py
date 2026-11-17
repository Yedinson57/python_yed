# Lista de estudiantes
estudiantes = ["Carlos","Ana","Luis"]

# Guardamos en estudiantes.txt
with open("estudiantes.txt", "w") as f: #"w"/write Abrimos el archivo en modo escritura
    for estudiante in estudiantes:
        f.write(estudiante + "\n")
        
# Leemos el archivo e imprimimos con número
with open("estudiantes.txt", "r") as f: # "r"/read Abrimos el archivo en modo lectura
    for i, linea in enumerate(f, start=1):
        print(f"{i} {linea.strip()}") # .strip() elimina los saltos de linea invisibles al imprimir
# ---

# Agregamos a "Marta" sin borrar lo anterior usando el modo append ("a") anexar
with open("estudiantes.txt","a") as f:
    f.write("Marta\n")
    
# Leemos el archivo y contamos cuantos estudiantes hay
with open("estudiantes.txt","r") as f:
    lineas = f.readlines() # Cargamos todas las lineas del archivo en una lista de Python
    print(f"Hay {len(lineas)} estudiantes en total.") # Usamos len para saber la cantidad total de elementos
    
# Leemos nuevamente el archivo y mostramos la lista con el nuevo agregado
with open("estudiantes.txt", "r") as f: # "r"/read Abrimos el archivo en modo lectura
    for i, linea in enumerate(f, start=1):
        print(f"{i} {linea.strip()}") # .strip() elimina los saltos de linea invisibles al imprimir