# 30 - Crie um programa que leia um número inteiro
# e mostre na tela se ele é PAR ou ÍMPAR.

from time import sleep

num = int(input('Entre com um número: '))

print('PROCESSANDO...')
sleep(1)

if (num % 2 == 0):
    print('ESSE NÚMERO É PAR')
else:
    print('ESSE NÚMERO É ÍMPAR')