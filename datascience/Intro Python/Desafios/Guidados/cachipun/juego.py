import sys
import random

jugadas = ["piedra","tijera","papel"]
jugada = sys.argv[1].lower()
jugada_pc = random.choice(jugadas).lower()

if jugada not in jugadas:
    print('Argumento inválido: Debe ser piedra, papel o tijera.')
else:
    print(f'Tu jugaste {jugada}.')
    print(f'Computadora jugó {jugada_pc}.')

    if jugada == jugada_pc:
        print('Empate!!')
    elif (jugada == "piedra" and jugada_pc == "tijera") or (jugada == "papel" and jugada_pc == "piedra") or (jugada == "tijera" and jugada_pc == "papel"):
        print('Ganaste!!')
    else:
        print('Perdiste!!')