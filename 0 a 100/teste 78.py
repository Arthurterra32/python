times = ('Palmeiras', 'Internacional', 'Flamengo', 'Fluminense', 'Corinthians', 'Athletico-PR', 
'Atlético-MG' ,'América-MG', 'Fortaleza', 'Botafogo', 'Santos', 'São Paulo', 'Bragantino',
'Goiás', 'Coritiba', 'Ceará', 'Cuiabá', 'Atlético-GO', 'Avaí', 'Juventude')
print('-=' * 30)
print(f'Lista de times do brasileirao: {times}')
print('-=' * 30)
print (f'Os cinco primeiros times sao: {times[:5]}')
print('-=' * 30)
print(f'Os quatro ultimes times sao: {times[-4:]}')
print('-=' * 30)
print(f'Times em ordem alfabetica: {sorted(times)}')
print('-=' * 30)
print(f'O time do santos esta na {times.index("Santos")+1}ª posicao')
