print('-='*20)
print('Analisador de triangulos')
print('-='*20)
r1 = float(input('primeiro segmento:')) 
r2 = float(input('segundo segmento:')) 
r3 = float(input('terceito segmento:'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('os segmentos acime podem formar triangulo!')
else:
    print('os segmentos acima nao pode formar um triangulo')

