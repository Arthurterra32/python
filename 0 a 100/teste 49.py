from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0, 2)
print('''
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Sua opcao: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!')
print('-='*15)
print('Computador jogou {}'.format(itens[pc]))
print ('Jogador jogou {}'.format(itens[jogador]))
print('-='*15)
if pc == 0:
    if jogador ==0:
        print('EMPATE')
    elif jogador ==1:
        print('JOGADOR VENCE')
    elif jogador ==2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGAVA INVALIDA')
elif pc == 1:
    if jogador ==0:
        print('COMPUTADOR VENCE')
    elif jogador ==1:
        print('EMPATE')
    elif jogador ==2:
        print('JOGADOR VENCE')
    else:
        print('JOGAVA INVALIDA')
elif pc == 2:
    if jogador ==0:
        print('JOGADOR VENCE')
    elif jogador ==1:
        print('COMPUTADOR VENCE')
    elif jogador ==2:
        print('EMPATE')
    else:
        print('JOGAVA INVALIDA')
