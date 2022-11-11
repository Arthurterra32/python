def aumentar(preco=0, taxa=0, form=False):
    res = preco + (preco * taxa /100)
    if form == False:
        return res
    else:
        return moeda(res)


def diminuir(preco, taxa=0, form=False):
    res = preco - (preco * taxa/100)
    if form == False:
        return res
    else:
        return moeda(res)

    

def dobro(preco=0, form=False):
    res = preco * 2
    if form == False:
        return res
    else:
        return moeda(res)


def metade(preco=0, form=False):
    res = preco / 2
    if form == False:
        return res
    else:
        return moeda(res)



def moeda(preco, moeda='R$'):
    return f'{moeda}{preco:>.2f}'.replace('.', ',')


def resumo(preco, aumento, reducao):
    print('-' * 35)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-' * 35)
    print(f'Preco analisado: \t{moeda(preco)}')
    print(f'Dobro do preco: \t{dobro(preco, True)}')
    print(f'Metade do preco: \t{metade(preco, True)}')
    print(f'{aumento}% de aumento: \t{aumentar(preco, aumento, True)}')
    print(f'{reducao}% de reducao: \t{diminuir(preco, reducao, True)}')
    print('-' * 35)
