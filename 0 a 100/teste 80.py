num = (int(input('Digite um numero: ')), int(input('Digite outro numero: ')), 
int(input('Digite mais um numero: ')), int(input('Digite o ultimo numero: ')), )
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1}ª posicao')
else:
    print('O valor 3 nao foi digitado em nenhuma posicao')
print('Os valores pares digitados foram ', end='')
for par in num:
    if par % 2 == 0:
        print(par, end=' ')
