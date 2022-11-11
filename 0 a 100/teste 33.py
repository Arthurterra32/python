vel = float(input('qual a velocidade em km/h do carro?'))
if vel > 80:
    print('MULTADO! Voce exxcedeu o limite permitido que e de 80km/h')
    multa = (vel-80)*7
    print('Voce de pagar uma multa de R${:.2f}'.format(multa))
else:
    print('Tenha um bom dia! Dririja com seguranca!')
