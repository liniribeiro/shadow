class Conta:

    """
    A programação procedural pode causar duplicidade de código, mal entendimento do negócio e dificil manutenabilidade.
    É indicado, para aplicações mais robustas a Programação Orientada a Objetos.
    """
    def __init__(self, numero, titular, saldo, limite):
        # O atributo fica privado com dois  __ -> encapsulamento - acesso aos atributos a partir de métodos.
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo {} do titular {}".format(self.__saldo, self.__titular))

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)

    def get_saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    def set_saldo(self, valor):
        self.__saldo = valor

    @limite.setter
    def limite(self, valor):
        self.__limite = valor

    @staticmethod
    def banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {'bb': "001", 'bradesco': '123'}

