num = int(input('digite um numero:'))
unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10
print('unidade {}'.format(unidade))
print('dezena {}'.format(dezena))
print('centena {}'.format(centena))
print('mlihar {}'.format(milhar))
