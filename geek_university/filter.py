"""
Filter - Filtrar dados de uma determinada coleção
"""
import statistics

data = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calculando a média dos dados utilizando a função mean() - Média

media = statistics.mean(data)
print(f" Média : {media}")

# Assim como a func map, a filter recebe dois parametros. Uma função e um iterável.
# Lambda recebe cada vez um dos dados de data e o filter pega apenas os dados que forem maioes que a média
res = filter(lambda x: x > media, data)

print(list(res))


uses = [
    {
        'username': 'samuel',
        "tweets": ["eu adoro bolas", "meus amigos sao legais"]
    }, {
        'username': 'carla',
        "tweets": []
    }, {
        'username': 'jeff',
        "tweets": []
    }, {
        'username': 'bob123',
        "tweets": ["eu adoro bolas"]
    }
]

print(uses)
# Filtrar usuarios que estao inativos

# inactives = list(filter(lambda u : len(u['tweets']) == 0, uses))
inactives = list(filter(lambda u : not u['tweets'], uses))
print(inactives)

# Combinar filter e map -  Criar uma lista onde os nomes tenham menos de 5 caracteres

names = ['Vanessa', 'Ana', 'Maria']

lista = list(map(lambda name: f"Sua instrutora é: {name}", filter(lambda name: len(name) < 5, names)))
print(lista)

