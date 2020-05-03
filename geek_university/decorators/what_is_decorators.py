"""
    Decorators

    - São functions
    - Envolvem outras functtions e aprrimoram seus comportamentos
    - Sã exemplos de HOP
    - Possui uma sintaxe própria - sugar sintax


    É o aprimoramento das functions

"""
# Não recomendado

def seja_educado(function):
    def sendo():
        print("Foi um prazer!")
        function()
        print("Tenha um ótimo diia")

    return sendo


def saudacao():
    print("Seja bem vinda Alini")

teste = seja_educado(saudacao)

teste()

# Recomendado


def seja_educado_mesmo(function):
    def sendo_mesmo():
        print("Foi um prazer conhecer voce mesmo!")
        function()
        print("Tenha um ótimo diia")

    return sendo_mesmo


@seja_educado_mesmo
def apresentando():
    print("Meu nome é Pedro")


apresentando()

print("-------")
"""
Decorators sempre pecisam receber functions com apenas 1 parametro. Para + de 1 parametro é utilizado o decorator pattern.
args e kwargs
"""

def gritar(function):
    def aumentar(*args, **kwargs):
        return function(*args, **kwargs).upper()
    return aumentar


@gritar
def saud(name):
    return f"Olá, eu sou {name}"


@gritar
def ordenar(princ, acompa):
    return f"Olá, eu gostaria de {princ} com { acompa}"


print(ordenar('jujuba', 'castanha'))
print(saud("alini"))