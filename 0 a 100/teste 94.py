lista = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1:'))
    nota2 = float(input('Nota 1:'))
    media = (nota1 + nota2) / 2
    lista.append([nome , [nota1 , nota2], media])
    next = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if next in 'N':
        break
for i, a in enumerate(lista):
    print(f' {i:<4} {a[0]:<10} {a[2]:>8.1f}')
while True:
    escolha = int(input('Mostrar notas de qual aluno? (999 interrompe):'))
    if escolha == 999:
        break
    if escolha <= len(lista) -1:
        print(f'Nota de {lista[escolha][0]} sao {lista[escolha][1]}')