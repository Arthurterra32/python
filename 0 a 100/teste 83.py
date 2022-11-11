lista = []
maior = 0
menor = 0
for count in range(0,5):
    lista.append(int(input('Digite um valor:')))
    if count == 0:
        maior = lista[count]
        menor = lista[count]
    else:
        if lista[count] > maior:
            maior = lista[count]
        if lista[count] < menor:
            menor = lista[count]
print(f'Voce digitou os valores {lista}')
print(f'O maior valor digitado foi {max(lista)} nas posicaoes ', end='')
for posicao, valor in enumerate(lista):
    if valor == maior:
        print(f'{posicao}...', end='')
print(f'\nO menor valor digitado foi {min(lista)} nas posicaoes ', end='')
for posicao, valor in enumerate(lista):
    if valor == menor:
        print(f'{posicao}...', end='')