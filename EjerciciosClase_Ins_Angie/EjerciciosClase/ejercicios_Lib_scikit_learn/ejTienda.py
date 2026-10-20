import pandas as pd
from sklearn.tree import DecisionTreeClassifier

df = pd.read_excel("ejemplo.xlsx")

print(df)

mapeo_compra = {"Si": 1, "No": 0}
df["Puede comprar"] = df["Puede comprar"].map(mapeo_compra)

x = df[["Precios"]]
y = df["Puede comprar"] 

modelo = DecisionTreeClassifier(random_state=42)
modelo.fit(x, y)

dinero = input("cuanto dinero ha gastado: ")

nuevo_cliente = [[dinero]]

prediccion = modelo.predict(nuevo_cliente)

if prediccion [0]==1:
    print("El cliente puede comprar")
else:
    print("El cliente no podria comprar")