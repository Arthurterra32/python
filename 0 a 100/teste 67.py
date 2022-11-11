num = int(input('Digite um numero: '))
count = 0
n1 = 1
n2 = 1
while count < num:
    n3 = n1 + n2     #2    #3   #5
    print(n3)
    count += 1
    n1 = n2          #1    #2   #3
    n2 = n3          #2    #3   #5