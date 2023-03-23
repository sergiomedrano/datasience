import requests
import json
from imprimir import imprimir_fotos

api_key = 'D7D5jghStlZKP92wPfA0zvDXC2jiaj4jjXyHOyjv'
url =  'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key=' + api_key

response = requests.get(url)
fotos = json.loads(response.text)

imprimir_fotos(fotos['photos'][:25])