def factorial(n):
    f = 1
    [f := f * i for i in reversed(range(1,n+1))]
    print(f'El factorial de {n} es {f}')

def productoria(lista):
    p = 1
    [p := p*int(i) for i in lista]
    print(f'La productoria de {lista} es {p}')

def calcular(**kwargs):
    for k,v in kwargs.items():
        if isinstance(v,int):
            factorial(v)
        elif isinstance(v,list):
            productoria(v)
        else:
            print(f'{v} tiene un tipo de dato incorrecto({type(v)}).')
            exit()

# main
calcular(fact_1 = 5,prod_1 = [4,6,7,4,3], fact_2 = 6, f = 'Perro')