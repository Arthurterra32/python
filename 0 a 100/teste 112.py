def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO: por favor, digite um numero inteiro valido.')
        except KeyboardInterrupt:
            print('\nO usuario preferiu nao digitar esse numero.')
            return 0
        else:
            return n
  
def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('ERRO: por favor, digite um numero real valido.')
        except KeyboardInterrupt:
            print('\nO usuario preferiu nao digitar esse numero.')
            return 0
        else:
            return n


inteiro = leiaint('Digite um numero inteiro: ')
real = leiafloat('Digite um numero real: ')
print(f'O valor inteiro digitado foi {inteiro} e o real foi {real}')