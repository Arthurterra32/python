from random import choice
nome1 = str(input('digite o nome do primeiro aluno:'))
nome2 = str(input('digite o nome do segundo aluno:'))
nome3 = str(input('digite o nome do terceito aluno:'))
nome4 = str(input('digite o nome do quarto aluno:'))
lista = [nome1,nome2,nome3,nome4]
escolhido = choice(lista)
print('o aluno escolhido foi {}'.format(escolhido))