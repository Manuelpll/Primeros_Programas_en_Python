import requests

# Realiza una llamada a la API y verifica la respuesta.
url = "https://api.github.com/search/repositories?q=language:python+sort:stars+stars:>10000"
headers = {"Accept": "application/vnd.github.v3+json"}

# Realizar la solicitud GET
r = requests.get(url, headers=headers)

# Imprimir el código de estado de la respuesta
print(f"Status code: {r.status_code}")

# Convierte el objeto de respuesta en un diccionario.
response_dict = r.json()

# Procesa los resultados: Imprimir las claves del diccionario de respuesta
print(response_dict.keys())
print(f"Total repositories: {response_dict['total_count']}")

# Verificar si los resultados están completos
print(f"Complete results: {not response_dict['incomplete_results']}")

# Explora la información sobre los repositorios
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

# Examina el primer repositorio
repo_dict = repo_dicts[0]
print(f"\nKeys: {len(repo_dict)}")

# Imprimir las claves del primer repositorio
for key in sorted(repo_dict.keys()):
    print(key)
#Informacion del primer repositorio
repo_dict = repo_dicts[0]

print("\nSelected information about the first repository:")
print(f"Name: {repo_dict['name']}")
print(f"Owner: {repo_dict['owner']['login']}")
print(f"Stars: {repo_dict['stargazers_count']}")
print(f"Repository: {repo_dict['html_url']}")
print(f"Created: {repo_dict['created_at']}")
print(f"Updated: {repo_dict['updated_at']}")
print(f"Description: {repo_dict['description']}")

# Explora la información sobre los repositorios.
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

print("\nSelected information about each repository:")

for repo_dict in repo_dicts:
    print(f"\nName: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Description: {repo_dict['description']}")
