# 17. Faça um programa que leia o comprimento do cateto oposto
# e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.

import math

co = float(input('Entre com o valor do cateto oposto: '))
ca = float(input('Entre com o valor do cateto adjacente: '))
hip = math.hypot(ca, co)
print('Com o cateto oposto valedo {} e o adjacente valendo {}, '
      'a hipotenusa vale {}'.format(co, ca, hip))

'''hip = (co**2 + ca**2) ** (1/2)
print('Com o cateto oposto valedo {} e o adjacente valendo {}, '
      'a hipotenusa vale {}'.format(co, ca, hip))'''