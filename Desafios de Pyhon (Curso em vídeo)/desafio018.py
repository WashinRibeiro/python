# 18. Faça um programa que leia um ângulo qualquer e mostre
# na tela o valor do seno, cosseno e tangente desse ângulo.

from math import radians, sin, cos, tan

angulo = float(input('Digite o ângulo que deseja: '))
sen = sin(radians(angulo))
cos = cos(radians(angulo))
tan = tan(radians(angulo))
print('{}° em radianos equivale a \nSENO = {:.2f}, '
      '\nCOSSENO = {:.2f} e \nTANGENTE = {:.2f}'.format(angulo, sen, cos, tan))
