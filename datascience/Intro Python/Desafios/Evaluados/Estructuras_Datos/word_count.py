import sys

archivo = open(sys.argv[1])
texto = archivo.read()

caracteres_diferentes = len(set(texto))
palabras_diferentes = len(set(texto.split(sep=" ")))

print(f'El número de caracteres distintos es: {caracteres_diferentes}')
print(f'El número de palabras distintas es: {palabras_diferentes}')