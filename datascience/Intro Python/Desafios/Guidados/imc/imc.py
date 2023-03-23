# imc = w / h**2

# Bajo peso: < 18.5
# Adecuado: 18.5 y 25
# Sobrepeso: 25 y 30
# Obesidad Grado I: 30 y 35 
# Obesidad Grado II: 35 y 40
# Obesidad Grado II: > 40

import sys

w = int(sys.argv[1]) # En kg
h = float(sys.argv[2])/100 # En cm

if h <= 0 or w <= 0:
    print('Ingrese valores mayor a 0.')
else:
    imc = w/(h**2)

    if imc > 0 and imc < 18.5:
        clasificacion = 'Bajo Peso'
    elif imc >= 18.5 and imc < 25:
        clasificacion = 'Adecuado'
    elif imc >= 25 and imc < 30:
        clasificacion = 'Sobrepeso'
    elif imc >= 30 and imc < 35:
        clasificacion = 'Obesidad Grado I'
    elif imc >= 35 and imc <= 40:
        clasificacion = 'Obesidad Grado II'
    else:
        clasificacion = 'Obesidad Grado III'
    
    print(f'Su IMC es {imc:.2f} [Kg/m2]')
    print(f'La clasificación OMS es {clasificacion}')