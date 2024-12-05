import requests
import plotly.express as px

# Hace una llamada a la API y verifica la respuesta.
url = "https://api.github.com/search/repositories?q=language:python+sort:stars+stars:>10000"
headers = {"Accept": "application/vnd.github.v3+json"}

# Realiza la solicitud GET a la API
r = requests.get(url, headers=headers)

# Imprime el código de estado de la respuesta
print(f"Status code: {r.status_code}")

# Procesa los resultados totales
response_dict = r.json()
print(f"Complete results: {not response_dict['incomplete_results']}")

# Procesa la información del repositorio
repo_dicts = response_dict['items']
repo_names, stars = [], []

for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

# Crea la visualización con Plotly
fig = px.bar(x=repo_names, y=stars, title="Most Starred Python Repositories on GitHub",
             labels={'x': 'Repository', 'y': 'Stars'}, template="plotly_dark")
fig.show()
title = "Most-Starred Python Projects on GitHub"
labels = {'x': 'Repository', 'y': 'Stars'}

# Crear la visualización con Plotly Express
fig = px.bar(x=repo_names, y=stars, title=title, labels=labels)

# Actualizar el diseño de la gráfica
fig.update_layout(
    title_font_size=28,
    xaxis_title_font_size=20,
    yaxis_title_font_size=20
)

# Mostrar la gráfica
fig.show()

# Definir las listas para los nombres de los repositorios, estrellas y textos emergentes
repo_names, stars, hover_texts = [], [], []

# Procesar la información de los repositorios
for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

    # Construir los textos emergentes
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    hover_text = f"Owner: {owner}<br />Description: {description}"
    hover_texts.append(hover_text)

# Crear la visualización
title = "Most-Starred Python Projects on GitHub"
labels = {'x': 'Repository', 'y': 'Stars'}

fig = px.bar(x=repo_names, y=stars, title=title, labels=labels, hover_name=hover_texts)

# Actualizar el diseño de la gráfica
fig.update_layout(
    title_font_size=28,
    xaxis_title_font_size=20,
    yaxis_title_font_size=20
)

# Mostrar la gráfica
fig.show()

# Inicializar las listas para los enlaces de los repositorios, estrellas y textos emergentes
repo_links, stars, hover_texts = [], [], []

# Procesar los datos de los repositorios
for repo_dict in repo_dicts:
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    # Crear el enlace activo del repositorio
    repo_link = f'<a href="{repo_url}">{repo_name}</a>'
    repo_links.append(repo_link)

    stars.append(repo_dict['stargazers_count'])

    # Crear el texto emergente (hover text)
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    hover_text = f"Owner: {owner}<br />Description: {description}"
    hover_texts.append(hover_text)

# Crear la visualización
title = "Most-Starred Python Projects on GitHub"
labels = {'x': 'Repository', 'y': 'Stars'}

fig = px.bar(x=repo_links, y=stars, title=title, labels=labels, hover_name=hover_texts)

# Actualizar el diseño de la gráfica
fig.update_layout(
    title_font_size=28,
    xaxis_title_font_size=20,
    yaxis_title_font_size=20
)

# Mostrar la gráfica
fig.show()

fig.update_layout(
    title_font_size=28,
    xaxis_title_font_size=20,
    yaxis_title_font_size=20
)

# Actualizar el color y la opacidad de las barras
fig.update_traces(
    marker_color='Green',  # Color de las barras
    marker_opacity=0.86  # Opacidad de las barras (valor entre 0 y 1)
)

fig.show()