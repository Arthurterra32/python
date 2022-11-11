l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))

def area(larg, comp):
    a = larg * comp
    print(f'A area de um terreno de {larg}x{comp} e de {a}m²')

area(l, c)