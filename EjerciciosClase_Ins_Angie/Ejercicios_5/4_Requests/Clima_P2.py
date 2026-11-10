import requests

# Definimos el método para consultar el clima
def consultar_clima(lat, lon):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "current": "temperature_2m,wind_speed_10m"
    }
    try:
        # Agregamos timeout=10 para cortar la conexión si tarda mas de 10 segundos
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status() # Para detectar errores del servidor HTTP
        return response.json()
    # Bloque except para mostrar el mensaje y devolver none en caso de fallo de red o mala URL sin detener el script
    except requests.exceptions.RequestException as e:
        print(f"Error de conexión al consultar las coordenadas ({lat}, {lon}): {e}")
        return None

# Prueba de funcionamiento
resultado = consultar_clima(2.4419, -76.6063)
if resultado:
    print("Consulta exitosa:", resultado["current"])