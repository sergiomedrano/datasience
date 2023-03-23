import sys

def consulta_precios(precios, precio, umbral):
    if umbral == 'mayor':
        productos = [k for k, v in precios.items() if v >= precio]
    elif umbral == 'menor':
        productos = [k for k, v in precios.items() if v <= precio]
    else:
        productos = [k for k, v in precios.items() if v > precio]
    
    return ', '.join(productos)

# main
umbrales = ['mayor','menor','']
precios = {'Notebook': 700000,
           'Teclado': 25000,
           'Mouse': 12000,
           'Monitor': 250000,
           'Escritorio': 135000,
           'Tarjeta de Video': 1500000}

precio = int(sys.argv[1])
umbral = sys.argv[2] if len(sys.argv) == 3 else ''

if umbral not in umbrales or precio <= 0:
    print('Lo sentimos, no es una operación válida')
    exit()

print(f'Los productos mayores al umbral son: {consulta_precios(precios, precio, umbral)}')