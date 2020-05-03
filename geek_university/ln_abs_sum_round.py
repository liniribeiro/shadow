"""
    Len, ABS, Sum, Round

    len() -> Numero de itens de um iterável

    abs() ->  Valor absoluto de um numero inteeiro  ou real (Os numeros sempre são positivos)

    sum() ->  recebe um iteravel e podendo receber um valor inicial, retorna a soma de todos os lementos, incluindo o valor inicial
    Valor nicial default é 0.

    round() - >  retorna um numero arredondado, se a precisão nao for informada, retorna o inteiro mais proximo
"""

print(abs(-5))
print(abs(3.14))


print(sum([1, 3, 4, 5, 2]))
print(sum([1, 3, 4, 5, 2], 5))
print(sum([1, 3, 4, 5, 2], -5))

print(sum([1.768578, 3.675867, 4.7684]))


print(round(10.2))
print(round(10.5))
print(round(10.6))
print(round(10.212121, 2))
print(round(10.219999, 2))