count = 0
soma = 0
while True:
    num = int(input('Digite um valor (999 para parar): '))
    if num == 999:
        break
    soma += num
    count += 1
print(f'{count} numeros foram digitados e a soma entre ele foi {soma}!')
