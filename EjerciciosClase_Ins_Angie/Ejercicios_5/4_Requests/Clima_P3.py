import json
import requests

def consultar_clima(lat, lon):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "current": "temperature_2m,wind_speed_10m"
    }
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

# Realizamos una consulta y guardamos en clima.json mediante json.dump()
datos_clima = consultar_clima(2.4419, -76.6063)
if datos_clima:
    with open("clima.json", "w", encoding="utf-8") as f:
        json.dump(datos_clima, f, indent=4, ensure_ascii=False)

# Leemos el archivo mediante jspn.load() y mostramos solo la temperatura actual
with open("clima.json", "r", encoding="utf-8") as f:
    clima_leido = json.load(f)
    temperatura = clima_leido["current"]["temperature_2m"]
    unidad = clima_leido["current_units"]["temperature_2m"]
    print(f"Temperatura extraída del archivo: {temperatura} {unidad}")