import requests

# URL de la API para obtener información de Pikachu
url = "https://pokeapi.co/api/v2/pokemon/snivy"

# Hacer la petición GET
response = requests.get(url)

# Verificar si la respuesta fue exitosa (código 200)
if response.status_code == 200:
    data = response.json()

    print("Keys disponibles:")
    for key in data.keys():
        print("-", key)
    # Extraer información relevante
    nombre = data["name"]
    altura = data["height"]
    peso = data["weight"]
    tipos = [t["type"]["name"] for t in data["types"]]

    # Mostrar resultados
    print(f"Nombre: {nombre.capitalize()}")
    print(f"Altura: {altura / 10} m")
    print(f"Peso: {peso / 10} kg")
    print(f"Tipos: {', '.join(tipos)}")
else:
    print("Error al obtener los datos")