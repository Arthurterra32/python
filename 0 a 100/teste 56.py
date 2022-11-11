num = int(input('Digite um numero: '))
total = 0
for count in range(1, num + 1):
    if num % count == 0:
        print('\033[33m', end= '')
        total += 1
    else:
        print('\033[31m', end= '')    
    print('{}'.format(count))
print('\n\033[mO numero {} foi divisivel {} vezes'.format(num, total))
if total == 2:
    print('E por isso ele e PRIMO!')
else:
    print('E por isso ele nao e PRIMO!')
