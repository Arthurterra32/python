from random import randint
lista = []
final = []
vezes = int(input('Quantos jogos voce quer que eu sorteie? '))
total = 1
while total <= vezes:
    count = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            count += 1
        if count >= 6:
            break
    lista.sort()
    final.append(lista[:])
    lista.clear()
    total += 1
for i, l in enumerate(final):
    print(f'jogo {i+1} {l}')