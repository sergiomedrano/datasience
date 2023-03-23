import preguntas as p
import random
from shuffle import shuffle_alt

# Opciones dadas para escoger.
###############################################
opciones = {'basicas': [1,2,3],
            'intermedias': [1,2,3],
            'avanzadas': [1,2,3]}
###############################################

def choose_q(dificultad):
    #escoger preguntas por dificultad
    preguntas = p.pool_preguntas[dificultad]
    
    # usar opciones desde ambiente global
    opciones = [k for k,v in p_global[dificultad].items()]
    
    # escoger una pregunta
    n_elegido = random.choice(opciones)
    pregunta = preguntas[n_elegido]
    
    # eliminarla del ambiente global para no escogerla de nuevo
    p_global[dificultad].pop(n_elegido)
    
    # escoger enunciado y alternativas mezcladas
    alternativas = []
    for k,v in pregunta.items():
        if k == 'alternativas':
            random.shuffle(v)
            alternativas = v
    
    return pregunta['enunciado'], alternativas

#main
global p_global
p_global = p.pool_preguntas

if __name__ == '__main__':
    # si ejecuto el programa, las preguntas cambian de orden, pero nunca debieran repetirse
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')
    
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')
    
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')