# ve = sqrt(2gr)
# ve = Velocidad Escape (m/s)
# g = constante gravitacional (m/s2)
# r = radio del planeta (m)

import math

g = float(input('Ingrese la constante g: '))
r = int(input('Ingrese el radio en kilometros: '))

ve = round(math.sqrt(2*g*(r*1000)),2)

print(f'La Velocidad de Escape es {ve} [m/s]')