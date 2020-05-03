"""
    Módulo Randon

    Módulos são arquivos .py - Cada arquivo é um módulo
    São uteis para reutilizar código

    Módulo random possui varias funçoes para gerações de numeros pseudo-aleatorio

    Existe 2 formas de utilizar o módulo
    1 - Importando todo o modulo (todos os atributosficam em memória) - Não recomendado
    2-


    python console:
    import random
    dir(random)
    help(random.random)
"""
from random import random, uniform, randint, choice, shuffle

# Random gera valores aleatórios

for i in range(10):
    print(random())

# Uniform gera valores aleatórios pré estabelecisos

print("Uniform")
for i in range(10):
    print(uniform(3, 7))

print("Randint")
# randint gera valores inteiros
for i in range(4):
    print(randint(1, 60), end=', ')


print("\nChoise")
# choice  -> Mostra um valor aleatório entre iteravel
jogadas = ['pedra', 'papel', 'tesoura']
print(choice(jogadas))
print(choice("Alini Ribeiro"))

print("Shuffle")
# shuffle  -> Embaralha as cartas 
cartas = ['K', 'Q', 'J']
print(cartas)
shuffle(cartas)
print(cartas)

