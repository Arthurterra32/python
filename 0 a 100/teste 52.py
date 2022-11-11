soma = 0
cont = 0
for impar in range(1, 501, 2):
    if impar % 3 == 0:
        soma += impar
        cont += 1
print('A soma de todos os {} valores solicitados e {}'.format(cont, soma))



# soma = soma + impar