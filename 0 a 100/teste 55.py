termo = int(input('Digite o primeiro termo: '))
razao = int (input('Digite a razao: '))
ultimo = termo + (10-1)*razao
ultimo = ultimo + 1
if razao > 0:
    for var in range(termo, ultimo, razao):
        print(var, end=' → ')
    print('Progessao aritimetica CRESCENTE'.format(var))
elif razao < 0:
    for var in range(termo, ultimo, razao):
        print(var, end=' → ')
    print('Progessao aritimetica DECRESCENTE'.format(var))
elif razao == 0:
    for var in range(0, 10):
        print(termo, end=' → ')
    print('Progessao aritimetica CONSTANTE'.format(var))
