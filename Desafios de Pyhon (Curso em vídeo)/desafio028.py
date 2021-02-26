# 29 - Escreva um programa que faça o computador “pensar”
# em um número inteiro entre 0 e 5 e peça para o usuário
# tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep

aleatorio = randint(0, 5) #número que o computador pensou
print('-=-' * 20)
print('Vou pensar em um número de 0 a 5, tente adivinhar...')
print('-=-' * 20)
num = input(('Qual número estou pensando? ')) #número que pessoa vai colocar
print('PROCESSANDO...')
sleep(2)

if num == aleatorio:
    print('VOCÊ VENCEU!!! Meus parabéns!!')
else:
    print('VOCÊ PERDEU. Tente novamente... ')
