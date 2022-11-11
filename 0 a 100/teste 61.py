sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite seu sexo: ')).upper().strip()
    if len(sexo) > 1:
        sexo = ''