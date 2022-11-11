contagem = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco',' seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezeseis', 'dezesete', 'dezeoito', 'dezenove', 'vinte')
while True:
    num = int(input('Digite um numero entre 0 e 20: '))
    if num >= 0 and num <= 20:
        print(f'Voce digitou o numero {contagem[num]}')
