termo = int(input('Digite o primeiro termo: '))
razao = int (input('Digite a razao: '))
ultimo = termo + 10*razao
count = 10
pa = ''
while termo < ultimo and razao > 0:
    termo += razao
    pa = 'crescente'
    print(termo, end=' → ')
while termo > ultimo and razao < 0:
    termo += razao
    pa = 'decrescente'
    print(termo, end=' → ')
while razao == 0 and count > 0:
    count -= 1
    pa = 'constante'
    print(termo, end=' → ')
print('Progessao aritimetica {}'.format(pa))
