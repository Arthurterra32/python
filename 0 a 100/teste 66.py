termo = int(input('Digite o primeiro termo: '))
razao = int (input('Digite a razao: '))
count = 0
vezes = 10
while count < vezes:
    termo += razao
    count += 1
    print(termo, end=' → ')
    if count == vezes:
        count2 = int(input('quanto x mais?'))
        vezes += count2



# if count == vezes:
# vezes += int(input('quanto x mais?'))