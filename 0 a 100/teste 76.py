contagem = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco',' seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezeseis', 'dezesete', 'dezeoito', 'dezenove', 'vinte')
num = int(input('Digite um numero entre 0 e 20: '))
for cont in range (0, len(contagem)):
    while num < 0 or num >= 21:
        num = int(input('Tente novamente. Digite um numero entre 0 e 20: '))
    if num == cont:
        print(f'Voce digitou o numero {contagem[cont]}')
