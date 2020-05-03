"""
Zip - Cria um iteravel que agrega elemento de cada um dos iteráveis passados como entrada em pares?????

ele pega oo primeiro elemento da lista 1 e o primeiro elemento da lista 2 e gera pares : [(1, 4), (2, 5), (3, 6)]

"""

list1 = [1, 2, 3]
list2 = [4, 5, 6]

zip1 = zip(list1, list2)
print(zip1)
print(type(zip1))

# Sempre podemos gerar uma list, tuple set or dict

print(list(zip1))
print(tuple(zip1))
print(set(zip1))
print(dict(zip1))


prova1 = [10, 9]
prova2 = [2, 4]
alunos = ['maria', 'alini']

final = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}
print(final)

# com map
final = zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2)))

print(dict(final))