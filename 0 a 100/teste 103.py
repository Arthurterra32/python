from time import sleep

def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    
    if passo == 0:
        passo = 1
    print(f'Contagem de {inicio} ate {fim} de {passo} em {passo}')
    
    if inicio < fim:
        count = inicio
        while count <= fim:
            print(f'{count} ', end='')
            sleep(0.2)
            count += passo
    
    else:
        count = inicio
        while count >= fim:
            print(f'{count} ', end='')
            sleep(0.2)
            count -= passo

contador(1, 10, 1)
print()
contador(10, 0, 2)
print()

i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

contador(i, f, p)