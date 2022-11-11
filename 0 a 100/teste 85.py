lista = []
for count in range(1,6):
    num = int(input(f'{count}° numero: '))
    if count == 1 or num > lista[-1]:
        lista.append(num)
    else:
        posicao = 0
        while posicao < len(lista):
            if num < lista[posicao]:
                lista.insert(posicao, num)
                break
            posicao += 1
print(f'Os valores digitados em ordem foram {lista}')
