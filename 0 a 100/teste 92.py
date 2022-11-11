lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapares = 0
somacoluna = 0
maior = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        lista[linha][coluna] = int(input(f'Digite um numero para [{linha}, {coluna}]:'))
        if lista[linha][coluna] % 2 == 0:
            somapares += lista[linha][coluna]
        if coluna == 2:
            somacoluna += lista[linha][coluna]
        if linha == 1:
            maior = lista[linha][0]
            if lista[linha][coluna] > maior:
                maior = lista[linha][coluna]
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{lista[linha][coluna]:^5}]', end='')
    print()
print(f'A soma de todos os valores pares {somapares}')
print(f'A soma dos valores da terceira coluna {somacoluna}')
print(f'O maior valor da segunda coluna {maior}')