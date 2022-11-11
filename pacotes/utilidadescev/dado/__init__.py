def leiadinheiro(msg):
    ok = False
    while True:
        n = str(input(msg)).replace(',', '.').strip()
        if n.isalpha() or n == '':
            print('Erro!! {n} e um preco invalido!')
        else:
            ok = True
            return float(n)