num = 0
count = 0
soma = 0
while num != 999:
    soma += num
    num = int(input('Digite um numero: '))
    count += 1
print('{} numeros foram digitados e a soma e igual a {}'.format(count, soma))