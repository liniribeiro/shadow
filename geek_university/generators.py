"""
Generators consomen menos recurso em memória que um list Comprehention

Generators limpam a memória depois de ter sido executados

Deve ser utilizado o generators caso não precise deste dado para manipulação depois.
"""
import time
from sys import getsizeof

names = ['Alini', 'Barbara', 'Amanda', 'Alice']
print(any(name[0] == 'B' for name in names))

# List Comprehention
res = [name[0] == 'B' for name in names]
print(type(res))
print(res)

# Generators
res = (name[0] == 'B' for name in names)
print(type(res))
print(res)

# getsizeof retorna a quantidade de bytes em memória do objeto, quanto maior a string, mais espaço ocupa
print(getsizeof('Alini Ribeiro'))
print(getsizeof(True))
print(getsizeof(2))

list_comp = getsizeof([x * 10 for x in range(1000)])
print(f"Size off list_comp: {list_comp}")
set_comp = getsizeof({x * 10 for x in range(1000)})
print(f"Size off set_comp: {set_comp}")
dict_comp = getsizeof({x: x * 10 for x in range(1000)})
print(f"Size off dict_comp: {dict_comp}")
gen_comp = getsizeof((x * 10 for x in range(1000)))
print(f"Size off gen_comp: {gen_comp}")


# iterando Gen
gen_comp = (x * 10 for x in range(10))
for num in gen_comp:
    print(num)

print("-------------------")
'''
    Generators podem ser criados com funções gradoras
    Funções geradoras utilizam a palavra reservada yield
    Generators podem ser criados com expressões geradoras
    
    Diferençãs entre funçãos e generator functions
    
    `````````````````````````````````````````````````````````````````````````````````````
    | Functions                           | Generaor Functions                           
    `````````````````````````````````````````````````````````````````````````````````````
    | utilizam return                     | utilizam yield                                
     ````````````````````````````````````````````````````````````````````````````````````
    | retorna uma vez                     | pode utilizar yield multiplas vezes           
    ````````````````````````````````````````````````````````````````````````````````````
    | quando executada, retorna um valor  | retrna um generator        
    ````````````````````````````````````````````````````````````````````````````````````  
    
    yield sempre fica esperando um next
'''

# # Função geradora - Gera um generator
# def first_yeld_example(max_value):
#     cont = 1
#     while cont <= max_value:
#         yield cont
#         cont +=1
#
#
# gen = first_yeld_example(5)
# # print(type(gen))
# # print(next(gen))
# # print(next(gen))
# # print(next(gen))
# # print(next(gen))
#
# # for num in gen:
# #     print(num)
#
# """
#     Teste de memória com generators
#
#     Seequencia fibonacci: 1, 1, 2, 3, 5, 8, 13
# """
#
# # 3 MB
# def fibon_gen(max):
#     a, b, contador = 0, 1, 0
#     while contador < max:
#         a, b = b, a + b
#         yield a
#         contador += 1
#
# # 440 MB
# def fibon_normal(max):
#     nums = []
#     a, b = 0, 1
#     while len(nums) < max:
#         nums.append(b)
#         a, b = b, a + b
#     return nums
#
#
# for n in fibon_gen(3):
#     print(n)
#
# print("-------------------")
#
# '''
#     Teste de velocidade com Expressões geradoras
#
# '''
#
#
# # Generators
# def nums():
#     for num in range(1, 5):
#         yield num
#
# gen = nums()
# # Generator
# print(gen)
#
# # Generator expression
#
# gen2 = (num for num in range(1, 5))
# print(gen2)
# print(next(gen2))
# print(next(gen2))
# print(next(gen2))
#
# print(sum(num for num in range(1, 10)))
#
# # Teste de velocidade
#
# # Generator expression
# gen_init = time.time()
# print(sum(num for num in range(1, 100000000)))
# gen_final = time.time() - gen_init
#
# # List Comprehention
# gen_init2 = time.time()
# print(sum([num for num in range(1, 100000000)]))
# gen_final2 = time.time() - gen_init
#
# print(f"Generator eexpression : {gen_final}")
# print(f"List Comprehention : {gen_final2}")



from itertools import islice



def split_every(n, iterable):
    i = iter(iterable)
    piece = list(islice(i, n))
    while piece:
        yield piece
        piece = list(islice(i, n))


def nums():
    for num in range(1, 670):
        yield num

gen = nums()
splited = split_every(5, gen)

for x in splited:
    print(x)