import requests


class SearchAddress:
    def __init__(self, cep):
        if self.validate(cep):
            self.cep = cep
        else:
            ValueError("CEP inválido")

    def __str__(self):
        return self.format()

    def format(self):
        return f"{self.cep[:5]}-{self.cep[5:]}"


    @staticmethod
    def validate(cep):
        if not len(cep) == 8:
            return False
        return True

    def get_by_cep(self):
        url = f"https://viacep.com.br/ws/{self.cep}/json/"
        a = requests.get(url).json()
        return [a['bairro'], a['localidade'], a['uf']]
