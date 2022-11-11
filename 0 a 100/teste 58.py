from datetime import date
ano = date.today().year
maior = 0
menor = 0
for rept in range(0, 3):
    nascimento = int(input('Qual a data de nascimento: '))
    idade = ano - nascimento
    if idade < 21:
        menor += 1
    else:
        maior += 1
print('''{} pessoas sao de menor  
{} pessoas sao de maior'''.format(menor, maior))