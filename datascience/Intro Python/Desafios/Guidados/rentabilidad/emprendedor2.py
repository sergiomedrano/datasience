#Utilidades = P * (Unormal + (Upremium*1.5)) - GT
#P = Precio suscripción
#Unormal = Usuarios normales
#Upremium = Usuarios premium
#GT = Gastos Totales

print('NOTA: Solo ingresar valores numéricos.')
p = int(input('Ingrese el Precio de suscripción: '))
u_normal = int(input('Ingrese la cantidad de usuarios normales: '))
u_premium = int(input('Ingrese la cantidad de usuarios premium: '))
gt = int(input('Ingrese los gastos totales: '))

u = p * (u_normal + (u_premium*1.5)) - gt

print(f'La utilidad es: {int(u)}')