import pandas as pd

inventario = {
    "producto": ["Camisa", "Gorra", "Pantalón", "Medias", "Zapatos"],
    "precio": [45000, 30000, 89000, 8000, 150000],
    "stock": [20, 5, 12, 40, 3],
}

# Forma (shape) y nombre de las columnas
df = pd.DataFrame(inventario)
print(df)
print("Forma",df.shape)
print("Nombres de las columnas",list(df.columns)) # Nombres de las columnas convertidos en listas
print(df.describe())

# productos por reponer con stock menor a 10
print("Porductos con bajo stock")
bajo_stock = df[df["stock"] < 10]
print(bajo_stock)

# columna valor (precio * stock) y otra columna True si se necesita reponer
print("Valor inventario")
df["valor_inventario"] = df["precio"] * df["stock"]
df["reponer"] = df["stock"] < 10
print(df)

# ordenar el inventario del mas caro al mas barato(sort_values)
print("Ordenar y resumir")
df_ordenado = df.sort_values(by="precio", ascending=False)
print("Inventario ordenado del mas caro al mas barato:")
print(df_ordenado)

# Precio promedio de los productos
precio_prom = df["precio"].mean()
print(f"Precio promedio de todos los productos: ${precio_prom:,.2f}")

# Guardar el DataFrame ecomo un archivo CSV, leer y verificar que los datos sean iguales
print("leer datos desde un archivo")
df.to_csv("inventario.csv", index = False)
print("DataFrame guardado como 'inventario.csv'")

df_leido = pd.read_csv("inventario.csv")
print("Datos leidos desde el archivo csv:")
print(df_leido)

son_iguales = df.equals(df_leido)
print(f"Los datos originales y leidos son iguales?: {son_iguales}")
