# 16. Crie um programa que leia um número Real qualquer
# pelo teclado e mostre na tela a sua porção Inteira.

'''from math import trunc
num = float(input('Entre com um valor real: '))
int = trunc(num)
print('A parte inteira de {} é {}'.format(num, int))'''

num = float(input('Entre com um valor real: '))
print('A parte inteira de {} é {}'.format(num, int(num)))
