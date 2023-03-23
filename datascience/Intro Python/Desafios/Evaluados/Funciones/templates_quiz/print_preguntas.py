import preguntas as p
import string

def print_pregunta(enunciado, alternativas):
    
    abc = string.ascii_uppercase
    
    print(f'- {enunciado[0]}')
    for a,v in alternativas:
        print(f'{abc[alternativas.index([a,v])]}. {a}')
        
if __name__ == '__main__':
    # Las preguntas y alternativas deben mostrarse según lo indicado
    pregunta = p.pool_preguntas['basicas']['pregunta_1']
    print_pregunta(pregunta['enunciado'],pregunta['alternativas'])
    
    # Enunciado básico 1

    # A. alt_1
    # B. alt_2
    # C. alt_3
    # D. alt_4