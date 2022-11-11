temp = []
lista = []
count = 0
maior = 0
menor = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(int(input('Peso: ')))
    if len(lista) == 0:
        menor = temp[1]
        maior = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    lista.append(temp[:])
    temp.clear()
    count += 1
    next = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if next in 'N':
        break
print(f'{count} pessoas foram cadastradas')
print(f'O maior peso foi de {maior}kg. Peso de ', end='')
for p in lista:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
print(f'\nO menor peso foi de {menor}kg. Peso de ', end='')
for p in lista:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')
