from random import randint

numeros = []

def sorteia(lista):
    for count in range(0, 5):
        numeros.append(randint(1, 10))
    print(f'Os numeros sorteados foram {numeros}')

def somapar(lista):
    total = 0
    for valor in numeros:
        if valor % 2 == 0:
            total += valor
    print(f'A soma dos pares e {total}')


sorteia(numeros)
somapar(numeros)
