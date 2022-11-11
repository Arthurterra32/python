lista = []
pares = []
impares = []
while True:
    lista.append(int(input('Digite um valor:')))
    next = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if next in 'N':
        break
for indice, valor in enumerate(lista):
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)
print(f'A lista completa e {lista}')
print(f'Os numeros pares da lista {pares}')
print(f'Os numeros impares da lista {impares}')
