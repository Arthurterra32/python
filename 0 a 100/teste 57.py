frase = str(input('Digite uma frase: ')).upper().strip()
palavras = frase.split() 
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('o inverso de {} e {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palindromo')
else:
    print('A frase digitada nao e um palindromo')





# INVERTER [::-1]