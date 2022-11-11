from random import randint
count = 0
while True:
    num = int(input('Diga um valor: '))
    pc = randint(1,10)
    soma = pc + num
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('[P/I] ')).strip().upper()[0]
    print(f'Voce jogou {num} e o pc jogou {pc}. Total de {soma} ', end='')
    print('DEU PAR' if soma % 2 == 0 else 'DEU IMPAR')
    if escolha == 'P':
        if soma % 2 == 0:
            print('Voce VENCEU!!!')
            count += 1
        else:
            print('Voce PERDEU!!!')
            break
    elif escolha == 'I':
        if soma % 2 == 1:
            print('Voce VENCEU!!!')
            count += 1
        else:
            print('Voce PERDEU!!!')
            break
print('Vamos jogar novamente...')
print(f'GAME OVER! Voce vendeu {count} vezes')
