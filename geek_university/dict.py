from collections import defaultdict, OrderedDict

'''
Lambdas são funções sem nomes que podem receber ujm valor de entrada e retornar valores
'''

'''
    Dict
'''

country = {'br': 'SC'}
print(country.get('sc', 'Não encontrado'))

localodades = {
    (35.666666, 76.88878): 'Escritório em Tókio',
    (35.666666, 56.88878): 'Escritório em Japão',
    (35.666666, 46.88878): 'Escritório em Coréia'
}

print(localodades)

country['eua'] = 'canada'
print(country)

# Atualizando dados em dicionário

country['eua'] = 'canadaaa'
print(country)

# Remover dado
country.pop('eua')
print(country)

carr = []
prod1 = {'name': 'prod1', 'qtd': 1, 'value': 300}
prod2 = {'name': 'prod2', 'qtd': 1, 'value': 300}

carr.append(prod1)
carr.append(prod2)
print(carr)

# Deep copy python, se alterar um valo do dicionado o outr nao muda
new = carr.copy()

# Shallow copy, se alterar o valor de carr, o new_shallow muda tbm.
new_shalow = carr

# métodos de dicionáripos

d = dict(a=1, b=2, c=3)
print(d)
d.clear()
print(d)

# From key recebe um iterável
user = {}.fromkeys(['nome', 'email', 'phone'], 'desconhecido')
print(user)


rec = {'jan': 100, 'fev': 300, 'mar': 400, 'abr': 500}

print(sum(rec.values()))
print(min(rec.values()))
print(max(rec.values()))


'''
    Default dict
'''
default_dict = defaultdict(lambda: 0)

default_dict['alini'] = 'OLÁ ALINI'

print(default_dict)

print(default_dict['alecio'])


'''
    Ordered Dict
'''

di1 = {'a': 1, 'b': 2}
di2 = {'b': 2, 'a': 1}
print(di1 == di2)

or_di1 = OrderedDict(di1)
or_di2 = OrderedDict(di2)
print(or_di1 == or_di2)
