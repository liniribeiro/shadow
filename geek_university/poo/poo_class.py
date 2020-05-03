"""
    Classes


    Quando nomeamoos as classes em Python, utilizamos o nome CamelCase
    Em python pode ter um arquivo com várias classes
"""


class Lampada():
    pass

lamp = Lampada()
print(type(lamp))

print("---- 12:44----")

"""
    Atributos - Carácterísticas do objeto
    
    
    Em python, dividimos os atributos em três grupos:
    - Atributos de Instância;
    - Atributos de Classe;
    - Atributos Dinâmicos.
    
    
    Atributos de Instância -> atributos declarados dentro do construtor
    
"""


class Lamp:

    def __init__(self, volt, color):
        self.volt = volt
        self.color = color
        self.oppen = False


class ContaCorrente:

    def __init__(self, numero, limite, saldo):
        self.limite = limite
        self.numero = numero
        self.saldo = saldo


class Produto:

    def __init__(self, nome, desc, valor):
        self.nome = nome
        self.desc = desc
        self.valor = valor


class Usuario:

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


