from pydoc import stripid


frase = str(input('digite uma frase:')).upper().strip
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A aparece na posicao {}'.format(frase.find('A')+1))
print('a ultima letra A apareceu na posicao {}'.format(frase.rfind('A')+1))