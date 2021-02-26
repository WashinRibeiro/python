# 23 - Faça um programa que leia um número de 0 a 9999
# e mostre na tela cada um dos dígitos separados

num = int(input('Entre com um número: '))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))

#------------------------------------------

'''Esse primeiro código está ainda com o erro pois não dá para fazer com menos de 4 algarísmos

num = str(input('Entre com um número: '))

dividido = num.split()
print('Unidade: {}'.format(num[3]))
print('Dezena: {}'.format(num[2]))
print('Centena: {}'.format(num[1]))
print('Milhar: {}'.format(num[0]))'''
