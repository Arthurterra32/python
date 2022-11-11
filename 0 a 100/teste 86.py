lista = []
count = 0
while True:
    lista.append(int(input('Digite um valor:')))
    count += 1
    next = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if next in 'N':
        break
print(f'{count} numeros foram digitados')
lista.sort(reverse=True)
print(f'A lista na ordem decrescente {lista}')
if 5 in lista:
    print('O valor 5 foi digitado e esta na lista')
else:
    print('O valor 5 nao digitado e nao na lista')

 