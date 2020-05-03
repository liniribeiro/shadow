"""
Sorted - podemos utilizar com qualquer iterável.
é diferente do sort() das listas

O sorted retorna uma nova lista
o Sort() ordena a lista passada

O sorted sempre retorna uma lista com os elementos do iterável retornados.

"""

numbers = [9, 6, 1, 8, 7]
print(numbers)

print(sorted(numbers))
print(sorted(numbers, reverse=True))
print(set(sorted(numbers, reverse=True)))

# Podemos utilizar para coisas mais complexas

users = [
    {
        'username': 'samuel',
        "tweets": ["eu adoro bolas", "meus amigos sao legais"]
    }, {
        'username': 'carla',
        "tweets": [],
        "cor":  "Preto",
        "musica": "BTS"
    }, {
        'username': 'jeff',
        "tweets": [],
        "cor":  "amarelo"
    }, {
        'username': 'bob123',
        "tweets": ["eu adoro bolas"]
    }
]
print(users)
print(sorted(users, key=len))
print(sorted(users, key=lambda user: user['username'], reverse=False))
