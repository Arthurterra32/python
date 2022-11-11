from asyncio import current_task


km = float(input('quantos kms de distancia tem a viagem:'))
if km <= 200:
    preco = km*0.50
else:
    preco = km*0.45
print('o preco da viagem sera R${:.2f}'.format(preco))