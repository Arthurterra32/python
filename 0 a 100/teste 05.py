from curses.ascii import isalpha
from unicodedata import numeric


n1 = int (input ('primeiro numero= '))
n2 = int (input ('segundo numero= '))
s = n1+n2
# print ('a soma entre', n1, 'e', n2, 'vale', s
print ('a soma entre {} e {} vale {}'.format(n1, n2, s))


# int numeros interios
# float numeros com ponto
# bool usado em True e False
# str usado em string
