print('-='*25)
print('Aprovador de emprestimos!!')
print('-='*25)
valor = float(input('Valor da casa: R$'))
salario = float(input('Qual o salario do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
meses = anos * 12
prestacao = valor/meses
if prestacao <= salario*0.3:
    print('Para pagar uma casa de R${:.2f} em {} anos a prestacao sera de R${:.2f}'.format(valor, anos ,prestacao))
    print('Emprestimo APROVADO!')
else:
    print('Para pagar uma casa de R${:.2f} em {} anos a prestacao sera de R${:.2f}'.format(valor, anos ,prestacao))
    print('Emprestimo NEGADO!')