nota1 = float(input('digite a primeira nota: '))
nota2 = float(input('digite a segunda nota: '))
media = (nota1 + nota2) / 2
if media < 5.0:
    print('''Sua media foi de {:.1f} 
    REPROVADO!'''.format(media))
elif media >= 7.0:
    print('''Sua media foi de {:.1f}
    APROVADO!'''.format(media))
elif 7> media >= 5:
    print('''Sua media foi de {:.1f}
    RECUPERACAO!'''.format(media))
