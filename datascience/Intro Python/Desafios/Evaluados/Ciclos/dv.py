serie = [2, 3, 4, 5, 6, 7]

rut = input("Ingresa tu RUT sin puntos ni dígito verificador: ")
listaRut = []
serie2 = []

# Se invierte rut y se almacena en una lista de int
# Se agregan los numeros necesarios a la serie
for i, n in enumerate(rut[::-1]):
    listaRut.append(int(n))
    if i < len(serie):
        serie2.append(serie[i])
    else:
        serie2.append(serie[i-len(serie)])

sum = 0
mult = 0
for i, n in enumerate(listaRut):
    for j, m in enumerate(serie2):
        if i == j:
            mult = m*n
            break
    sum += mult

digito = 11-(sum%11)
if digito == 10:
    dv = 'K'
elif digito == 11:
    dv = '0'
else:
    dv = f'{digito}'
    
print(f'Su dígito verificador es {dv}')