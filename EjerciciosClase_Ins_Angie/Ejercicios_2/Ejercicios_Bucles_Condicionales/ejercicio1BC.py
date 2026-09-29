# Recorre la lista de precios y aplica un 15% de descuento a aquellos valores superiores a 100000, imprimiendo el resultado
precios = [45000, 120000, 8000,300000]
porcentaje_descuento = 15

for precio in precios:
    if precio > 100000 :
        descuento = precio * (porcentaje_descuento / 100)
        precio_final = precio - descuento
        print(f"El precio final de {precio} con un descuento de {porcentaje_descuento}% es de: {precio_final}")