
"""
All - > Retorna true se todos os itens do iterável for verdadeiro ou vazio
"""

names = ['Alini', 'Ana', 'Amanda', 'Alice']

print(all(name[0] == 'A' for name in names))


"""
any - > Retorna true se um dos itens do iterável for verdadeiro ou vazio
"""

names = ['Alini', 'Barbara', 'Amanda', 'Alice']

print(any(name[0] == 'B' for name in names))