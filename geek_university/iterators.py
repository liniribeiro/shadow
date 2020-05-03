"""
Iterables e iterator

Iterator ->  Um objeto que pode ser iterado, um objeto qu retorna um dado, sendo um elemento por vez, quando a função next é chamada.
Iterable -> Um objeto que irá chamar um iterable quando a func iter(é chamada).
"""
# name é um iterable
name = "Alini"

# print(next(name)) Erro

it1 = iter(name)

print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))

"""
    Criando a própria versão do loop
"""


def my_for(itter):
    it = iter(itter)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break

my_for("alini")

"""
    Escrevendo iterator customizado
"""


class Contador:
    def __init__(self, menor, maior):
        self.menor = menor
        self.maior = maior

    def __iter__(self):
        return  self

    def __next__(self):
        if self.menor < self.maior:
            number = self.menor
            self.menor = self.menor + 1
            return number
        raise StopIteration


con = Contador(1, 61)

it = iter(con)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))