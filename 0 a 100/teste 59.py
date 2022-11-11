maior = 0
menor = 0
for rept in range (0, 3):
    peso = int(input('Qual e o seu peso: '))
    if rept == 0:
        maior = peso
        menor = peso
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print('{} {}'.format(menor, maior))
