time = []
jogador = {}
golstotal = []

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    golstotal.clear()
    for count in range(0, partidas):
        golstotal.append(int(input(f'Quantos gols na partida {count+1}: ')))
    jogador['gols'] = golstotal[:]
    jogador['total'] = sum(golstotal)
    time.append(jogador.copy())
    while True:
        next = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if next in 'SN':
             break
        print('Erro! Digite novamente')
    if next == 'N':
        break
print('-=' * 30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-=' * 30)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-=' * 30)
while True:
    busca = int(input('Mostra dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print('Erro! Digite novamente')
    else:
        print(f'Levantamento do jogador {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'No jogo {i+1} fez {g} gols')
        print('-=' * 30)
