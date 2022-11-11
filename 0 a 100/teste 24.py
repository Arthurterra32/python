from math import radians, sin, cos, tan
angulo = float(input('digite o angulo que voce deseja:'))
seno = sin(radians(angulo))
print('o angulo de {} tem o seno de {:.2f}'.format(angulo,seno))
cosseno = cos(radians(angulo))
print('o angulo de {} tem o cosseno de {:.2f}'.format(angulo,cosseno))
tangete = tan(radians(angulo))
print('o angulo de {} tem a tangente de {:.2f}'.format(angulo,tangete))