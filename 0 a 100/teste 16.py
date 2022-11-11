from re import A


salario = float(input('qual o seu salario?'))
novo = salario + (salario*15/100)
print('um funcionario que ganhava R${:.2f} com 15% de aumento, passsa a receber R${:.2f}'.format(salario,novo))