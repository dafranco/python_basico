import requests
import os

api_key = os.getenv('OPEN_WEATHER_API_KEY')
ciudad = 'Madrid'
url = f'http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric'

respuesta = requests.get(url)
print(respuesta)

if respuesta.status_code == 200:
    datos = respuesta.json()
    temperatura = datos['main']['temp']
    print(f"La temperatura actual en {ciudad} es de {temperatura}°C")
else:
    print("Error al obtener los datos de la API.")
