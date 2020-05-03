'''
Named tuple
'''
from collections import deque

from sqlalchemy.util import namedtuple

# Declarações
dog = namedtuple('dog', 'age racem name')

dog2 = namedtuple('dog', 'age, racem, name')

dog3 = namedtuple('dog', ['age', 'race', 'name'])

# Usando
ray = dog3(age=2, race='chau', name='Ray')
print(ray)

# Acessando
print(ray.age)
print(ray.name)
print(ray.index('Ray'))



'''
    Deque - Lista de alta performance
'''

# Criando

de = deque('geek')
print(de)

de.append('g')
print(de)

de.appendleft('k')
print(de)

print(de.popleft())