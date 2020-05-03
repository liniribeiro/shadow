"""
    Leitura de arquivos

    open() -> recebe apenas um parametro de entrada, na sua forma mais simples. Abre arquivo para leitura
"""



file_name = 'file_for_read.txt'
file = open(file_name)
# print(file.read())

'''
    Seeek - é utilizado para movimentar o cursor dentro do arquivo
'''
#
# file.seek(0)
# print(file.read())

# ler o arquivo linha alinha

lines = file.readlines()

print(len(lines))
print(lines)

file.close()


with open(file_name) as file:
    print(file.readlines())


with open('file_for_read_new.txt', 'w') as file:
    file.write('oi, estou sendo escrito pela alini')


with open(file_name) as file:
    print(file.readlines())


with open('vegetables.txt', 'w') as file:
    while True:
        veg = input('Informe um vegetal ou informe sair: ')
        if veg != 'sair':
            file.write(veg)
            file.write('\n')
        else:
            break


# a ->  append, adiciona SEMPRE o conteudo no final das linhas do arquivo que já exste
with open('vegetables.txt', 'a') as file:
    while True:
        veg = input('Informe um vegetal ou informe sair: ')
        if veg != 'sair':
            file.write(veg)
            file.write('\n')
        else:
            break


# +  -> abre no modo de atualização, leitura e escrita