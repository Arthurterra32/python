from datetime import date
funcionario = {}

funcionario['nome'] = str(input('Nome: '))
nascimento = int(input('Data de nascimento: '))
funcionario['idade'] = date.today().year - nascimento
funcionario['ctps'] = int(input('Carteira de Trabalho (0 nao tem): '))

if funcionario['ctps'] != 0:
    funcionario['ano da contratacao'] = int(input('Ano da contratacao: '))
    funcionario['salario'] = float(input('Seu salario: '))
    funcionario['aposentadoria'] = (funcionario['ano da contratacao'] - nascimento) + 35
print('-=' * 30)
for k, v in funcionario.items():
    print(f'O {k} tem o valor {v}')
