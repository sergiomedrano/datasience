def choose_level(n_pregunta, p_level):
    level = ''
    
    if p_level not in [1,2,3] or n_pregunta not in range(1,(3*p_level)+1):
       return level
    
    if n_pregunta <= 1*p_level:
        level = 'basicas'
    elif n_pregunta <= 2*p_level:
        level = 'intermedias'
    else:
        level = 'avanzadas'
        
    return level

if __name__ == '__main__':
    # verificar resultados
    print(choose_level(2, 2)) # básicas
    print(choose_level(3, 2)) # intermedias
    print(choose_level(6, 2)) # avanzadas
    print(choose_level(4, 3)) # intermedias