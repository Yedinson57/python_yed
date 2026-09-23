Estudiante = ("nombre", "edad", "curso")

# La modificacion no puede hacerse debido a que una tupla es inmutable, es decir
# NO SE PUEDE MODIFICAR, AÑADIR O ELIMINAR ELEMENTOS DESPUÉS DE CREARLA
Estudiante["curso"] = "cursor"

print(Estudiante)