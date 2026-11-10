# importamos requests
import requests

# url de la API
url = "https://api.open-meteo.com/v1/forecast"

# Parametros de latitud, longitud y las variables meteorologicas deseadas
params = {
    "latitude": 2.4419,
    "longitude": -76.6063,
    "current": "temperature_2m,wind_speed_10m"
}

# Usamos requests.get() enviando los parametros
response = requests.get(url, params=params)

# Convertimos la respuesta HTTP a un diccionario mediante .json()
data = response.json()

# Navegamos por sus claves para extraer la temperatura y el viento
temp = data["current"]["temperature_2m"]
wind = data["current"]["wind_speed_10m"]
temp_unit = data["current_units"]["temperature_2m"]
wind_unit = data["current_units"]["wind_speed_10m"]

# Imprimimos los resultados
print(f"Clima actual en Popayán:")
print(f"- Temperatura: {temp} {temp_unit}")
print(f"- Velocidad del viento: {wind} {wind_unit}")