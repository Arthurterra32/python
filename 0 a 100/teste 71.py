count = 1
tabuada = 0
num = int(input('Quer ver a tabuada de qual valor: '))
while True:
    tabuada = num * count
    print(f'{num} x {count} = {tabuada}')
    count += 1
    if count == 11:
        num = int(input('Quer ver a tabuada de qual valor: '))
        count = 1
    if num < 0:
        break
print(f'FIM!')
