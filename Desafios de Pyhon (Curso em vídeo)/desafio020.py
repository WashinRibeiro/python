# 20. O mesmo professor do desafio 19 quer sortear
# a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

n1 = str(input('Entre com o primeiro nome: '))
n2 = str(input('Entre com o segundo nome: '))
n3 = str(input('Entre com o terceiro nome: '))
n4 = str(input('Entre com o quarto nome: '))
lista = [n1, n2, n3, n4]
aleatorio = shuffle(lista) #random.shuffle embaralha o que foi selecionado nos parenteses
print('A ordem de apresentação será: ')
print(lista)