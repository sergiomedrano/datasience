import preguntas as p

def verificar(alternativas, eleccion):
    #devuelve el índice de elección dada
    if eleccion not in ['a', 'b', 'c','d']:
        return False
    
    eleccion = ['a', 'b', 'c','d'].index(eleccion)
    correcto = True if alternativas[eleccion][1] == 1 else False
    
    return correcto

if __name__ == '__main__':
    from print_preguntas import print_pregunta
    
    # Siempre que se escoja la alternativa con alt_2 estará correcta, e incorrecta en cualquier otro caso
    pregunta = p.pool_preguntas['basicas']['pregunta_2']
    print_pregunta(pregunta['enunciado'],pregunta['alternativas'])
    respuesta = input('Escoja la alternativa correcta:\n> ').lower()
    verificar(pregunta['alternativas'], respuesta)






