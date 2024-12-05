from operator import itemgetter
import requests

# Hace una llamada a la API y verifica la respuesta.
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)

# Verifica el código de estado de la respuesta
print(f"Status code: {r.status_code}")

# Procesa la información sobre cada envío
submission_ids = r.json()
submission_dicts = []

# Hace una nueva llamada a la API separada para cada envío
for submission_id in submission_ids[:30]:  # Limita a los 30 primeros
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")

    response_dict = r.json()

    # Crea un diccionario para cada artículo
    submission_dict = {
        'title': response_dict['title'],
        'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict.get('descendants', 0)  # Si no hay comentarios, se pone 0
    }

    submission_dicts.append(submission_dict)

# Ordena los diccionarios por el número de comentarios de forma descendente
submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

# Imprime los resultados
for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")
