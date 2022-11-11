lista = []
pessoas = {}
soma = 0
media = 0
while True:
    pessoas.clear()
    pessoas['nome'] = str(input('Nome: '))
    while True:
        pessoas['sexo'] = str(input('Sexo [M/F] ')).upper().strip()[0]
        if pessoas['sexo'] in 'MF':
            break
        print('Erro! Digite novamente')
    pessoas['idade'] = int(input('Idade: '))
    soma += pessoas['idade']
    lista.append(pessoas.copy())
    while True:
        next = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if next in 'SN':
            break
        print('Erro! Digite novamente')
    if next == 'N':
        break
print('-=' * 30)
print(f'Ao todo temos {len(lista)} pessoas cadastradas.')
media = soma / len(lista)
print(f'A media de idade e de {media:5.2f} anos')
print(f'As mulheres cadastradas foram ', end ='')
for p in lista:
    if p['sexo'] in 'F':
        print(f'{p["nome"]} ', end='')
print()
print(f'Lista das pessoas que estao acima da media ', end='')
for p in lista:
    if p['idade'] >= media:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')

