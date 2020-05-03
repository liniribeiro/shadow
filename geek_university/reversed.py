"""
Reversed

 Diferente da function reverse() das listas

 """


numbers = [1, 3, 5, 7, 90]
res = reversed(numbers)

print(res)
print(type(res))

print(list(reversed(numbers)))
# Set não armazena a ordem dos elementos (Conjunto)
print(set(reversed(numbers)))

print(tuple(reversed(numbers)))


for word in reversed("Alini Ribeiro"):
    print(word, end='')

print("\n")
print(''.join(list(reversed("Alini Ribeiro"))))
print("Alini Ribeiro"[::-1])
