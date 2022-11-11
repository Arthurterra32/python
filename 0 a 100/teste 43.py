from datetime import date
nascimento = int(input('data de nascimento: '))
atual = date.today().year
idade = atual - nascimento
if idade == 18:
    print('Voce precisa se alistar no exercito')
elif idade < 18:
    saldo = 18 - idade
    print('Quem nasceu em  {} tem {} anos em {}'.format(nascimento, idade, atual))
    ano = atual + saldo
    print('seu alistamento sera em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('voce ja deveria ter se alistado ha {} anos'.format(saldo))
    ano = atual - saldo
    print('seu alistamento foi em {}'.format(ano))
