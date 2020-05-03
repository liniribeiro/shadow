"""
    Lambdas
    Funções sem nome, funções anonimas.

"""
import math


def func(x):
    return 3 * x + 1


print(func(4))

# Expressao lambda
calc = lambda x: 3 * x + 1
print(calc(4))

nome = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()


# Ordena pelo sobtenome
autores = ['Alini Ribeiro', 'Guilherme Ribeiro', 'Alécio Gomes']
print(autores)
autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())
print(autores)

"""
    MAP:
    Com map, realizamos o mapeamento de valores para uma função
"""


def area(r):
    """Calcula a área de um circulo com raio r  (pi x r ao quadrado)"""
    return math.pi * (r ** 2)


raios = [2, 5, 7.1, 0.3, 10, 44]

areas = []
for r in raios:
    areas.append(area(r))


# Utilizando map  - Map é uma função que ecebe dois parametros: O primeiro é uma função e o segundo um iteravél. Retorna um map object

areas = (map(area, raios))
# Após utilizar a função mal, depois da pimeira utilizaçao do esultado, ele zera. aplicação = list(areas)


print(list(areas))

# Forma com lambda
print(list(map(lambda r: math.pi * (r ** 2), raios)))

# Exemplo 3
cidades = [('Berlin', 29), ('Cairo', 56), ('Tokio', 5)]
print(cidades)

# f = 9/5 * c + 32

cel_for_fa = lambda data: (data[0], (9/5) * data[1] + 32)
print(list(map(cel_for_fa, cidades)))
