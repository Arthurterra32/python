print('{:=^60}'.format(' LOJA DO MACACO '))
valor = float(input('Digite o valor do produto: R$'))
print('''Escolha a opcao de pagamento:
[ 1 ] A vista ou cheque: 10% de desconto
[ 2 ] A vista no cartao: 5% de desconto
[ 3 ] 2x no cartao sem juros
[ 4 ] 3x ou mais no cartao : 20% de juros''')
opcao = int(input('Sua opcao: '))
if opcao == 1:
    desconto = valor - (valor*10/100)
    print('A vista com 10% de desconto fica R${:.2f}'.format(desconto))
elif opcao == 2:
    desconto = valor - (valor*5/100)
    print('A vista no cartao com 5% de desconto fica R${:.2f}'.format(desconto))
elif opcao == 3:
    print('2x no cartao sem juros fica R${:.2f}'.format(valor))
elif opcao == 4:
    juros = valor + (valor*20/100)
    parcelatotal = int(input('Quantas parcelas? '))
    parcela = juros / parcelatotal
    print('''Sua com sera parcelada em {:.0f}x de R${:.2f}
    com juros de 20%'''.format(parcela ,juros))
else:
    print('Erro!! Tente novamente')

