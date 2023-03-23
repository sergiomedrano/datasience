#nombre
nombre = input('Ingrese su nombre: ')
#edad
edad = input('Ingrese su edad: ')
#actividades
actividades = []
i = 1
print('Ingrese 3 activiades que le guste realizar:')
while i <= 3:
    actividades.append(input(f'{i}.- '))
    i += 1
#tiene mascota?
tiene_mascota = input('Tiene mascotas (S/N): ').upper()

print(f'Nombre: {nombre}')
print(f'Edad: {edad}')
print(f'Una de sus actividades es: {actividades[1]}')

if tiene_mascota == 'S':
    tiene_mascota = 'Si'
elif tiene_mascota == 'N':
    tiene_mascota = 'No'
print(f'{tiene_mascota} tiene mascotas')

#tipos de datos
print(f'''
Los tipos de datos son:
    Nombre: {type(nombre)}
    Edad: {type(edad)}
    Actividades: {type(actividades)}
    Tiene mascota: {type(tiene_mascota)}''')

#presentacion
print(f'''
Mi nombre es {nombre}, tengo {edad} años,
mis actividades favoritas son {', '.join(actividades)}
y {tiene_mascota} tengo mascotas.     
''')