# Simulacion de un sistema de curso, con metodo de inscripcion si cumple la edad y metodo para listar estudiantes mayores de edad
class Curso:
    def __init__(self, nombre_curso):
        self.nombre_curso = nombre_curso
        self.estudiantes = []

    def inscribir(self, nombre, edad):
        if edad > 15:
            self.estudiantes.append({"nombre": nombre, "edad": edad})
            print(f"{nombre} (edad: {edad}) ha sido inscrito correctamente.")
        else:
            print(f"{nombre} (edad: {edad}) no cumple el requisito de edad (>15 años).")

    def listar_mayores_edad(self):
        # List comprehension para obtener solo los nombres de los mayores de 18 años
        return [e["nombre"] for e in self.estudiantes if e["edad"] > 18]

# Pruebas del reto
curso_python = Curso("Programación en Python")

# Intentos de inscripción
curso_python.inscribir("Pedro", 14)  # Rechazado
curso_python.inscribir("Sofia", 16)  # Inscrito
curso_python.inscribir("Juan", 22)   # Inscrito
curso_python.inscribir("Maria", 19)  # Inscrito

# Listar estudiantes mayores de 18 años
mayores = curso_python.listar_mayores_edad()
print("\nEstudiantes mayores de 18 años:", mayores)  # ['Juan', 'Maria']