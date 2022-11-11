import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com.br')
except:
    print('O site Pudim nao esta acessivel no momento.')
else:
    print('Consegui acessar o site Pudim com sucesso!')