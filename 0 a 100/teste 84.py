lista = []
while True:
    num = int(input('Digite um valor:'))
    if num not in lista:
        lista.append(num)
    else:
        print(f'Valor duplicado')
    next = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if next in 'N':
        break
lista.sort()
print(f'Voce digitou os valores {lista}')