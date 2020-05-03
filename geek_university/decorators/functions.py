"""
    Funções de maior grandeza - Higher Order Funcions

    Significa que uma linguagem suporta HOF, indica que podemos ter functions que retornam outras functions
    de resoltadoos, ou até mesmo criar variaveis de tipo funcions nos nossos programas.


    Em python, as functions são cidadoses de primeira classe: de maior grandeza

"""

# Examples - Defnindo as functions
from random import choice


def somar(a, b):
    return a + b


def diminuir(a, b):
    return a - b


def calcular(a, b, func):
    return func(a, b)

# Testando

print(calcular(1, 2, somar))
print(calcular(6, 2, diminuir))

print(">>>Nested Functions")

"""
    No Python também podemos ter funções dentro de funções, que são conhecidas como Nested Funcions, 
    ou também Inner Functions: Funções internas
"""


def say_hi(person):
    def humor():
        return choice(("E ai", "Sai daqui", "Gosto muito de você"))

    return f"{humor()} {person}"


print(say_hi("Alini"))


def faz_me_rir():
    def rindo():
        return choice(("hahahahahha", "kkkkkkkk"))

    return rindo

rindo = faz_me_rir()
print(rindo())


"""
    Inner functions podem acessar o escopo de funcions externas
"""