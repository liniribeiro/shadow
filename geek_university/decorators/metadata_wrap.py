"""
    Metadados: são dados intrícicos em arquivos
    ex: extemnsão do arquivo


    Wraps: functions que envolvem elementos com muitas funcionalidades | São funções



# Problema


def ver_log(func):
    def logger(*args, **kwargs):
        eu sou uma função logger dentro de outra
        print(f"Voce está chamando: { func.__name__}")
        print(f"Documentação: {func.__doc__}")
        return func(*args, **kwargs)

    return logger


@ver_log
def soma(a, b):
   Soma dois números
    return a + b


print(soma(10, 30))


"""

# Resolução
from functools import wraps


def ver_log(func):
    @wraps(func)
    def logger(*args, **kwargs):
        """eu sou uma função logger dentro de outra"""
        print(f"Voce está chamando: { func.__name__}")
        print(f"Documentação: {func.__doc__}")
        return func(*args, **kwargs)

    return logger


@ver_log
def soma(a, b):
    """Soma dois números"""
    return a + b


print(soma(10, 30))

print(soma.__name__)
print(soma.__doc__)
