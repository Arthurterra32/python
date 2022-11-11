def notas(*num, sit=False):
    cont = 0
    maior = 0
    menor = 0
    total = 0
    for valor in num:
        if cont == 0:
            maior = valor
            menor = valor
        else:
            if valor > maior:
                maior = valor
            if valor < menor:
                menor = valor
        total += valor
        cont += 1
        media = total / cont
    dic = {'total': cont, 'maior': maior, 'menor': menor, 'media': media}
    if sit == True:
        if media > 6:
            dic['situacao'] = 'Boa'
        if media >= 5 and media <= 6:
            dic['situacao'] = 'Razoavel'
        if media < 5:
            dic['situacao'] = 'Ruim'
    return dic


resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)