import requests
import json

# Hace una llamada a la API y guarda la respuesta.
url = "https://hacker-news.firebaseio.com/v0/item/31353677.json"  # URL corregida (Firebase URL correcta)
r = requests.get(url)  # Se corrige el error en la llamada de la función requests.get

# Verifica el código de estado HTTP
print(f"Status code: {r.status_code}")

# Explora la estructura de los datos
response_dict = r.json()

# Convierte el objeto de respuesta a un formato JSON legible
response_string = json.dumps(response_dict, indent=4)

# Imprime el resultado
print(response_string)
