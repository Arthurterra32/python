num = 0
count = 0
continuar = ''
soma = 0
maior = 0
menor = 0
while continuar != 'N':
    num = int(input('Digite um numero: '))
    soma += num
    count += 1
    if count == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    continuar = str(input('Quer continuar: [S/N] ')).upper().strip()[0]
media = soma / count
print('voce digitou {} numeros e a media foi {}'.format(count, media))
print(' o maior valor foi {} e o menor foi {}'.format(maior, menor))
