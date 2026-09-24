# usamos una comprehension para obtener solo los nombres de los productos que cuesten menos de 50.000.
productos = [
    {"nombre": "Camisa", "precio": 45000},
    {"nombre": "Pantalón", "precio": 89000},
    {"nombre": "Media", "precio": 8000}
]

en_oferta = [p["nombre"] for p in productos if p["precio"] < 50000]
print(en_oferta)  # ['Camisa', 'Media']