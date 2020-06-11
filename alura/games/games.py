from alura.games import forca

print('********************************************')
print('Escolha seu jogo')
print('********************************************')


print('(1) Forca  (2) Advinhação)')

game = input('Qual seu jogo?')

if game == int(1):
    print('Jogando Forca')
    forca.run()
else:
    print('Jogando Adivinhação')