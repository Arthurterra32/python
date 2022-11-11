total = 0
p1000 = 0
barato = 0
nbarato = ' '
count = 0
while True:
    nome = str(input('Nome do Produto: '))
    preco = int(input('Preco: R$'))
    total += preco
    next = ' '
    count += 1
    if preco >= 1000:
        p1000 += 1
    if preco < barato or count == 1:
        barato = preco
        nbarato = nome
    while next not in 'SN':
        next = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if next == 'N':
        break
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {p1000} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nbarato} que custa R${barato:.2f}')
