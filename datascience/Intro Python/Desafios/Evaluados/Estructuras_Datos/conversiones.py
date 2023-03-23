# PEN: Sol Peruano 0.0046
# ARS: Peso Argentino 0.093
# USD: Dolar americano 0.00013

import sys

monedas = {"PEN":float(sys.argv[1]),"ARS":float(sys.argv[2]),"USD":float(sys.argv[3])}
clp = int(sys.argv[4])

print(f'Los {clp:.0f} pesos equivalen a:')
print(f'{monedas["PEN"]*clp} Soles')
print(f'{monedas["ARS"]*clp} Pesos Argentinos')
print(f'{monedas["USD"]*clp} Dólares')