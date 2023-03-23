from string import ascii_lowercase

clave = input('Ingrese la contraseña: ').lower()

intentos = 0

for x in clave:
    for y in ascii_lowercase:
        intentos += 1
        if x == y:
            break

print(f'La contraseña fue forzada en {intentos} intentos.')