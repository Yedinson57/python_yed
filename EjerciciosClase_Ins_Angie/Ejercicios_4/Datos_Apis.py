import numpy as np
import requests
from sklearn.linear_model import LinearRegression

# datos pa entrenar el modelo
X_train = np.array([[80, 10], [50, 25], [70, 15], [30, 30], [90, 5]]) # Humedad
y_train = np.array([22, 30, 25, 35, 20]) # velocidad del viento

# creo y entreno la regresion lineal
modelo = LinearRegression()
modelo.fit(X_train, y_train)
 
# api del clima de bogota
url = "https://api.open-meteo.com/v1/forecast?latitude=4.6097&longitude=-74.0817&current=relative_humidity_2m,wind_speed_10m"

respuesta = requests.get(url)

if respuesta.status_code == 200:
    datos_api = respuesta.json()
    
    # saco la humedad y el viento actual
    humedad_actual = datos_api["current"]["relative_humidity_2m"]
    viento_actual = datos_api["current"]["wind_speed_10m"]
    
    # meto los datos en un array para que el modelo los lea
    entrada_actual = np.array([[humedad_actual, viento_actual]])
    temperatura_predicha = modelo.predict(entrada_actual)
    
    # imprimo los resultados
    print(f"Humedad actual: {humedad_actual}%")
    print(f"Viento actual: {viento_actual} km/h")
    print(f"Temperatura estimada: {temperatura_predicha[0]:.2f} °C")
else:
    print("Error:", respuesta.status_code)