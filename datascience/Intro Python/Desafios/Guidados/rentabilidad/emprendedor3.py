#Utilidades = P * U - GT
#P = Precio suscripción
#U = Usuarios
#GT = Gastos Totales

print('NOTA: Solo ingresar valores numéricos.')
p = int(input('Ingrese el Precio de suscripción: '))
u = int(input('Ingrese la cantidad de usuarios: '))
gt = int(input('Ingrese los gastos totales: '))
u_anterior = int(input('Ingrese la utilidad obtenida el año anterior: '))

u = p * u - gt

razon = round(u / u_anterior,2)

print(f'La utilidad actual es: {u}\n Mientras que, la razón versus las del año anterior es {razon}')