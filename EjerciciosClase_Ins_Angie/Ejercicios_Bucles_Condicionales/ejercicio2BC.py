# Recorre la lista de edades e imprime acceso permitido o denegado dependiendo de si es o no mayor de edad
edades_fila = [16, 20, 15, 30, 12, 25]

for edades in edades_fila:
    if edades >= 18:
        print(f"edad: {edades} - Acceso permitido")
    else:
        print(f"edad: {edades} - Acceso denegado")