import sys
import random

jugadas = ["piedra","tijera","papel"]
jugada = sys.argv[1].lower()
jugadaPC = random.choice(jugadas).lower()

aQuienGana = {"piedra": "tijera", "tijera": "papel", "papel": "piedra"}

if jugada not in jugadas:
    print('Argumento inválido: Debe ser piedra, papel o tijera.')
else:
    print(f'Tu jugaste {jugada}.')
    print(f'Computadora jugó {jugadaPC}.')

    if jugada == jugadaPC:
        print('Empate!!')
    elif aQuienGana[jugada] == jugadaPC:
        print('Ganaste!!')
    else:
        print('Perdiste!!')