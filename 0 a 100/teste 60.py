somaidade = 0
idadevelho = 0
nomevelho = ''
mulheres = 0
qtpessoas = 3
for rep in range(0, qtpessoas):
    nome = str(input('Qual e o seu nome: '))
    idade = int(input('Qual a sua idade: '))
    sexo = str(input('Qual o seu sexo: '))
    somaidade += idade
    if idade > idadevelho and sexo == 'm':
        idadevelho = idade
        nomevelho = nome
    if sexo == 'f' and idade < 20:
        mulheres += 1
media = somaidade / qtpessoas
print('a media de idade do grupo e {:.2f}'.format(media))
print(' o homen mais velho e {} e tem {} anos'.format(nomevelho, idadevelho))
print('{} mulheres tem menos de 20 anos'.format(mulheres))