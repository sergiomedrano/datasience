import requests
import json

url = 'https://reqres.in/api/users'

#1.- Consultar usuarios

response = requests.get(url)
user_data = json.loads(response.text)

#['id', 'email', 'first_name', 'last_name', 'avatar']

print("1.- Usuarios:")
[print(d) for d in user_data['data']]

# 2.- crear usuario
payload = '''{
    "first_name": "Ignacio",
    "trabajo": "profesor"
}'''

response = requests.post(url,data=payload)
created_user = response.text
print(f'\n2.- Creación Usuario:\n{response}')
print(created_user)

#3.- actualizar usuario
payload = '''{
    "first_name": "morpheus",
    "residence": "zion"
}'''

response = requests.put(url,data=payload)
updated_user = response.text
print(f'\n3.- Actualización Usuario:\n{response}')
print(updated_user)

#4.- eliminar usuario
payload = '''{
    "first_name": "Tracey"
}'''

response = requests.delete(url,data=payload)
print(f'\n4.- Eliminación Usuario:\n{response}')
print(response.text)