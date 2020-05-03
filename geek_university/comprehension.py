'''
    Listas aninhadas
'''

list_a = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
#
# for list in list_a:
#     for num in list:
#         print(num)

# List comprehension TOP
[[print(value) for value in list] for list in list_a]


# Gerando uma matriz 3x3
table = [[number for number in range(1, 4)] for value in range(1, 4)]
print(table)

# Gerando jogadas para o jogo da velha
velha = [['X' if number % 2 == 0 else '0' for number in range(1, 4)] for value in range(1, 4)]
print(velha)

'''
    Dict
'''
rec = [100, 300, 400, 500, 500]

quadrados = {value: value ** 2 for value in rec}
print(quadrados)

