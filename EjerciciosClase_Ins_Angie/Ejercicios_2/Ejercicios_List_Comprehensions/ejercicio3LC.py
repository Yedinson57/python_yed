# usamos una comprehension con condición para quedarnos solo con los que contienen "@".
correos = ["ana@gmail.com", "luis", "carlos@hotmail.com", "sena"]

correos_validos = [correo for correo in correos if "@" in correo]
print(correos_validos)  # ['ana@gmail.com', 'carlos@hotmail.com']