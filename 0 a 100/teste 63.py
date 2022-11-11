n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro valor: '))
opcao = 0
while opcao != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos numeros
    [ 5 ] sair do programa''')
    opcao = int(input('Sua opcao: '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {} e {} e igual {}'.format(n1, n2, soma))
    elif opcao == 2:
        mult = n1 * n2
        print('A multiplicacao entre {} e {} e igual {}'.format(n1, n2, mult))
    elif opcao == 3:
        if n1 > n2:
            print('{} e maior que {}'.format(n1, n2))
        else:
            print('{} e maior que {}'.format(n2, n1))
    elif opcao == 4:
        n1 = int(input('Digite um numero: '))
        n2 = int(input('Digite outro valor: '))
    elif opcao == 5:
        print('Finaliando...')
    else:
        print('Opcao invalida!')
