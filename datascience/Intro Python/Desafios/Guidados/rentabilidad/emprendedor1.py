#Utilidades = P * U - GT
#P = Precio suscripción
#U = Usuarios
#GT = Gastos Totales

print('NOTA: Solo ingresar valores numéricos.')
p = int(input('Ingrese el Precio de suscripción: '))
u = int(input('Ingrese la cantidad de usuarios: '))
gt = int(input('Ingrese los gastos totales: '))

u = p * u - gt

print(f'La utilidad es: {u}')