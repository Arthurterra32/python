n1 = 0
n10 = 0
n20 = 0
n50 = 0
while True:
    valor = int(input('Que valor voce quer sacar? R$'))
    while valor != 0:
        if valor >= 50:
            valor -= 50
            n50 += 1
        elif valor >=20:
            valor -= 20
            n20 +=1
        elif valor >=10:
            valor -= 10
            n10 += 1
        elif valor >= 1:
            valor -= 1
            n1+= 1
    if valor == 0:
        break
print(f'Tota de {n50} cedulas de R$50')
print(f'Tota de {n20} cedulas de R$20')
print(f'Tota de {n10} cedulas de R$10')
print(f'Tota de {n1} cedulas de R$1')
