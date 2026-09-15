# Agenda de contactos
contactos = [{
    "nombre":"Saul",
    "numero":"3405768435",
    "nacimiento":"04/08/2002",
    "favorito":False
},
{
    "nombre":"Diego",
    "numero":"3105878435",
    "nacimiento":"02/09/2003",
    "favorito":True
},
{
    "nombre":"Maria",
    "numero":"3895468435",
    "nacimiento":"10/10/2002",
    "favorito":True
},
{
    "nombre":"William",
    "numero":"3405468435",
    "nacimiento":"14/09/2001",
    "favorito":False
}]

# Recorremos la lista e imprimimos nombre y numero
print("CONTACTOS:")

for contacto in contactos:
    print("Nombre:",contacto["nombre"])
    print("Numero:",contacto["numero"])
    print()
    
# Imprimimos los contactos favoritos
print("CONTACTOS FAVORITOS:")

for contacto in contactos:
    if contacto["favorito"] == True:
        print(contacto["nombre"])
        
# Mostramos cuantos contactos cumplen años en un mes
mes = "09"
contador = 0

for contacto in contactos:
    fecha = contacto["nacimiento"]
    
    # La fecha se encuentra en formato DD/MM/AAAA
    # por lo tanto separamos mediante .split() para que quede ["DD","MM","AA"]
    partes = fecha.split("/")
    
    # obtenemos el mes mediante indice y sumamos 1 al contador si hay alguien que cumpla años en un mes
    if partes[1] == mes:
        contador += 1
    
print()
print("Contactos que cumplen años en un mes", mes, ":", contador)

# Creamos una lista nueva solamente con los nombres
nombres = []

for contacto in contactos:
    nombres.append(contacto["nombre"])
    
print()
print("LISTA DE NOMBRES:")
print(nombres)

# Buscamos un contacto por su nombre y si existe mostramos su numero
buscar_nombre = input("\nIngrese el nombre que desea buscar: ")

encontrado = False

for contacto in contactos:
    # .lower() convierte ambos en minusculas
    if contacto["nombre"].lower() == buscar_nombre.lower():
        print("Numero",contacto["numero"])
        encontrado = True
        break
    elif encontrado == False:
        print("El contacto no existe")