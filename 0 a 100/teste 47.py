peso = float(input('Qual o seu peso: '))
altura = float(input('Qual sua altura: '))
imc = peso / (altura * altura)
if imc < 18.5:
    print('''o seu imc e de {:.1F}
    voce esta abaixo do peso'''.format(imc))
elif 18.5 <= imc < 25:
    print('''o seu imc e de {:.1F}
    voce esta no peso ideal'''.format(imc))
elif 25 <= imc < 30:
    print('''o seu imc e de {:.1F}
    voce esta com sobrepeso'''.format(imc))
elif 30 <= imc < 40:
    print('''o seu imc e de {:.1F}
    voce esta obeso'''.format(imc))
else:
    print('''o seu imc e de {:.1F}
    obesidade morbida'''.format(imc))
