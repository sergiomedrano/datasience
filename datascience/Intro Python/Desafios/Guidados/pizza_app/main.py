from masa import tipo_masa
from salsa import tipo_salsa
from add import agregar_ingrediente
from remove import quitar_ingrediente
from tiempo import estimar_tiempo
from show import mostrar_ingredientes
import datos as d
import time
import os
import sys

clear = 'cls' if sys.platform == 'win32' else 'clear'

ingredientes_orden = d.ingredientes

print('¡Gracias por ordenar con nosotros!')
while True:
    os.system(clear)
    opcion = int(input(d.menu))
    
    if opcion == 1:
        os.system(clear)
        eleccion = input(d.T_MASA).upper()
        ingredientes_orden = tipo_masa(ingredientes_orden, eleccion)
        print('')
    elif opcion == 2:
        os.system(clear)
        eleccion = input(d.T_SALSA).upper()
        ingredientes_orden = tipo_salsa(ingredientes_orden, eleccion)
        print('')
    elif opcion == 3:
        os.system(clear)
        eleccion = int(input(d.AG_INGREDIENTE)) 
        ingredientes_orden = agregar_ingrediente(ingredientes_orden, eleccion)
        print('')
    elif opcion == 4:
        os.system(clear)
        eleccion = int(input(d.QT_INGREDIENTE))
        ingredientes_orden = quitar_ingrediente(ingredientes_orden, eleccion)
        print('')
    elif opcion == 5:
        os.system(clear)
        tiempo = estimar_tiempo(ingredientes_orden)
        print(f'Su pizza estára lista en {tiempo} minutos')
        ordenar = input('Desea ordenar ahora? (S/N)').upper()
        print('')
        if ordenar == 'S':
            print('Gracias por ordenar en Pizza JAT')
            print('Disfrute su pizza')
            time.sleep(3)
            exit()
            
    elif opcion == 0:
        os.system(clear)
        mostrar_ingredientes(ingredientes_orden)
        time.sleep(3)
        print('')
    else:
        os.system(clear)
        print('Su pedido ha sido cancelado. Gracias por contactarse a Pizza JAT')
        time.sleep(3)
        exit()