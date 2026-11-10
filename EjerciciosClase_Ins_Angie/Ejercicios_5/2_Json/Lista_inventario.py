# Importamos json
import json

# Lista inventario
inventario = [
 {"producto": "Camisa", "precio": 45000, "stock": 20},
 {"producto": "Gorra", "precio": 30000, "stock": 5},
 {"producto": "Pantalón", "precio": 89000, "stock": 12},
 {"producto": "Medias", "precio": 8000, "stock": 40},
 {"producto": "Zapatos", "precio": 150000, "stock": 3},
]

# Guardamos y abrimos inventario.json en modo escritura
with open("inventario.json", "w", encoding="utf-8") as f: 
    # "json.dump" convierte la estructura de datos de python en formato JSON
    # "indent=4" ordena el archivo en sangrias legibles y "ensure_ascii=False" asegura que los caracteres especiales se mantengan intactos
    json.dump(inventario, f, indent=4, ensure_ascii=False)    
# ---

# Leemos el archivo
with open("inventario.json","r", encoding="utf-8") as f:
    inventario_leido = json.load(f) # json.load() toma el contenido del archivo JSON y lo desrealiza de vuelta a una lista de diccionarios
    
    print("Productos con stock menor a 10:")
    # Recorremos a lista y evaluamos el stock mediante if
    for item in inventario_leido:
        if item["stock"] < 10:
            print(f"{item['producto']}: {item['stock']} unidades")
            
# Agregamos "Bufanda"
inventario_leido.append({"producto": "Bufanda", "precio": 25000, "stock": 15})
    
# Guardamos nuevamente el archivo
with open("inventario.json", "w", encoding="utf-8") as f:
    json.dump(inventario_leido, f, indent=4, ensure_ascii=False)
    
print(f"Ahora hay {len(inventario_leido)} productos en total")