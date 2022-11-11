from random import randint
from time import sleep
pc = randint(0,5)
num = int(input('digite um numero:'))
sleep(1)
if num == pc:
    print('parabens voce acertou!')
else:
    print('voce errou o numero escolhido era {}'.format(pc))
