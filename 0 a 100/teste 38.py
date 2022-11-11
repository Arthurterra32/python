salario = float(input('digite o seu salario:'))
if salario <= 1250:
    aumento = salario + (salario*15/100)
    print ('o seu salario aumentou em 15% totalizando R${:.2f}'.format(aumento))
else:
    aumento = salario + (salario*10/100)
    print('o seu salario aumentou em 10% totalizando R${:.2f}'.format(aumento))