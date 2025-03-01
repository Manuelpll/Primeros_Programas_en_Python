import requests
import plotly.express as px
from collections import defaultdict

# URL para obtener la lista de Pokémon (ajustar límite si hay más)
url = "https://pokeapi.co/api/v2/pokemon?limit=1303"

# Hacer la petición GET
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    pokemon_list = data["results"]

    # Diccionario para contar Pokémon por tipo
    type_counts = defaultdict(int)

    # Obtener tipos de cada Pokémon
    for pokemon in pokemon_list:
        pokemon_data = requests.get(pokemon["url"]).json()

        for tipo in pokemon_data["types"]:
            type_name = tipo["type"]["name"]
            type_counts[type_name] += 1

    # Convertir a lista de diccionarios para Plotly
    type_data = [{"Tipo": key, "Cantidad": value} for key, value in type_counts.items()]

    # Crear gráfico de barras con Plotly
    fig = px.bar(type_data, x="Tipo", y="Cantidad", title="Cantidad de Pokémon por Tipo",
                 labels={"Tipo": "Tipo de Pokémon", "Cantidad": "Cantidad"}, color="Tipo")

    # Mostrar gráfico
    fig.show()

else:
    print("Error al obtener los datos de la API")
