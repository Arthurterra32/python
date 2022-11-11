lista = [[], []]
for count in range(1,8):
    num = int(input(f'Digite o {count}o valor:'))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)
lista[0].sort()
lista[1].sort()
print(f'Os valores pares {lista[0]}')
print(f'Os valores imapres {lista[1]}')