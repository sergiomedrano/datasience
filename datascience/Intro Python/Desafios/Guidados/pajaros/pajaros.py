import requests
import json
from imprimir import imprimir_pajaro

url = 'https://aves.ninjas.cl/api/birds'

response = requests.get(url)
pajaros = json.loads(response.text)

#print(pajaros[0].keys())
imprimir_pajaro(pajaros)
#[imprimir_pajaro(p) for p in pajaros]
#['uid', 'name', 'images', '_links', 'sort']