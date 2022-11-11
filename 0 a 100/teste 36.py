from datetime import date
ano = int(input('qual ano quer analizar? coloque 0 para o ano atual:'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 ==0:
    print('o ano {} e um ano bissexto!'.format(ano))
else:
    print('{} nao e um ano bissexto!'.format(ano))
