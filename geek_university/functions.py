
'''
    *args
    é uma tupla
'''
# *args ecebe os parametros como uma tupla
def sum_numbers(*args, **kwargs):
    return sum(args)


numeros = [1, 2, 3, 4, 5, 6, 7, 7, 8, 8]

print(sum_numbers(2, 3, 4))

# * avisa para o python desempacotar a coleção que foi passado
print(sum_numbers(*numeros))


'''
    **kwargs
    os parametros dentro de kwargs precisam ser nomeados
    é um dicionário
'''


def say_hello(**kwargs):
    if kwargs.get('alini'):
        print('Hello Alini')
    else:
        print('Hello Stranger')


say_hello(alini='alini')

# Desempacotamento de kwargs | Como se cada dado do meu dicionário fosse um parametro passado
name = {'alini': 'alini'}
say_hello(**name)