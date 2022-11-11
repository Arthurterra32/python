soma = 0
for rep in range(1, 7):
    num = int(input('Digite um numero: '))
    if num % 2 == 0:
        soma += num
print('A soma dos numeros solicitados e igual a {}'.format(soma))
