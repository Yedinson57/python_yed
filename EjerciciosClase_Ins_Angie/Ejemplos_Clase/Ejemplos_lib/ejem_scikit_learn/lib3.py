# Como se importan
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.linear_model import LogisticRegression
# from sklearn.neighbors import KNeighborsClassifier

# from sklearn.ensemble import RandomForestClassifier
# from sklearn.linear_model import LinearRegression
# from sklearn.tree import DecisionTreeClassifier

import numpy as np
from sklearn.linear_model import LinearRegression

x_metros_cuadrados = np.array([[50], [60], [80], [100], [120], [150]])

y_precios = np.array([150, 175, 220, 270, 320, 390])

modelo_prediccion = LinearRegression()
modelo_prediccion.fit(x_metros_cuadrados, y_precios)

nueva_casa = np.array([[90]])
precio_predicho = modelo_prediccion.predict(nueva_casa)
print(f"para una casa de 90m², el precio estimado es ${precio_predicho[0]:.2f} millones")


