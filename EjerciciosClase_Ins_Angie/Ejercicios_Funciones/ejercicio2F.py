# Una funcion que devuleva True o False si una contraseña tiene mas o menos de 8 carateres
def es_valida(contrasena):
    
    if len(contrasena) >= 8:
        return True
    else:
        return False
    
print(es_valida("hola1234"))