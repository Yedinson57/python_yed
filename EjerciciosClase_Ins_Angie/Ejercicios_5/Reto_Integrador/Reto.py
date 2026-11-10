# importamos json y requests
import json
import requests

# Definimos el método para consultar el clima
def consultar_clima(lat, lon):
    # Url de la API
    url = "https://api.open-meteo.com/v1/forecast"
    # Parametros de latitud, longitud y las variables metorologicas deseadas(current)
    params = {
        "latitude": lat,
        "longitude": lon,
        "current": "temperature_2m"
    }
    # Bloque try/exception si encuentra un error en los parametros o en la peticion a la url 
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status() # Para detectar errores del servidor HTTP
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Aviso: No se pudo consultar la ubicación ({lat}, {lon}). Detalle: {e}")
        return None

# Diccionario de ciudades colombianas con sus coordenadas
ciudades = {
    "Popayán": (2.4419, -76.6063),
    "Bogotá": (4.7110, -74.0721),
    "Cali": (3.4516, -76.5320),
    "Medellín": (6.2442, -75.5812)
}

clima_exitoso = {}

# Recorremos el diccionario y consultamos cada ciudad
for ciudad, coordenadas in ciudades.items():
    lat, lon = coordenadas
    print(f"Consultando clima para {ciudad}...")
    resultado = consultar_clima(lat, lon)
    
    if resultado:
        temp = resultado["current"]["temperature_2m"]
        unidad = resultado["current_units"]["temperature_2m"]
        clima_exitoso[ciudad] = f"{temp} {unidad}"
    else:
        print(f"Saltando {ciudad} debido a un error de conexión.\n")

# Guardamos los resultados exitosos en clima_ciudades.json
with open("clima_ciudades.json", "w", encoding="utf-8") as f:
    json.dump(clima_exitoso, f, indent=4, ensure_ascii=False)

# Leemos el archivo y mostramos cuál es la ciudad más calurosa
with open("clima_ciudades.json", "r", encoding="utf-8") as f:
    datos_guardados = json.load(f)

if datos_guardados:
    # Encontramos la ciudad con la temperatura máxima convirtiendo el texto a float
    # Mediante max() y key=lambda para separar numéricamente el valor de la temperatura de su unidad
    ciudad_mas_calurosa = max(datos_guardados, key=lambda c: float(datos_guardados[c].split()[0])) 
    temp_max = datos_guardados[ciudad_mas_calurosa]
    print(f"\nLa ciudad más calurosa es {ciudad_mas_calurosa} con una temperatura de {temp_max}.")
else:
    print("\nNo se pudieron obtener datos exitosos de ninguna ciudad.")