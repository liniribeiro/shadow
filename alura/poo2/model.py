class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    def dar_likes(self):
        self._likes +=1

    @property
    def likes(self):
        return self._likes

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, new_nome):
        self._nome = new_nome.title()

    def imprime(self):
        print(f'{self.nome} -  {self.ano}: {self.likes} Likes ')


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'{self.nome} -  {self.ano} - duração : {self.duracao} min: {self.likes} Likes '


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'{self.nome} -  {self.ano} - temporadas {self.temporadas} : {self.likes} Likes '


class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    def __len__(self):
        return len(self._programas)

    @property
    def lisgatem(self):
        return self._programas

    @property
    def tamanho(self):
        return len(self._programas)



vingadores = Filme("Vingadores - guerra infinita", 2018, 160)
panico = Filme("Panico - guerra infinita", 2018, 160)
atlanta = Serie("Atlanta", 2018, 2)
demolidor = Serie("demolidor", 2018, 2)

vingadores.dar_likes()
atlanta.dar_likes()
demolidor.dar_likes()
panico.dar_likes()
atlanta.dar_likes()

filmes_e_series = [vingadores, atlanta, demolidor, panico]

playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)

print(f"tamanho da listagem {len(playlist_fim_de_semana)}")
for prog in playlist_fim_de_semana.lisgatem:
    print(prog)