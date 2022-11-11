from random import randint
pc = randint(0,10)
tentativas = 1
num = int(input('Digite um numero: '))
while num != pc:
    num = int(input('tente novamente: '))
    tentativas += 1
print('o numero de tentativas foi {}'.format(tentativas))
print('voce ganhou!!!')

