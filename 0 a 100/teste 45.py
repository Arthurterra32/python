from datetime import date
ano = date.today().year
nascimeto = int(input('Qual a data de nascimeto: '))
idade = ano - nascimeto
if idade <= 9:
    print('''o atleta tem {} anos
    categoria MIRIM'''.format(idade))
elif idade <= 14:
    print('''o atleta tem {} anos
    categoria INFANTIL'''.format(idade))
elif idade <= 19:
    print('''o atleta tem {} anos
    categoria JUNIOR'''.format(idade))
elif idade <= 25:
    print('''o atleta tem {} anos
    categoria SENIOR'''.format(idade))
else:
    print('''o atleta tem {} anos
    categoria MASTER'''.format(idade))

