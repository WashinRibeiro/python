#4 - Faça um programa que leia algo pelo teclado e
#mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ela

algo = input('Digite um caracter: ')
print('O tipo primitivo desse caracter é: ', type(algo))
print('Esse caracter é um número? ', algo.isnumeric())
print('Esse caracter é alfabético? ', algo.isalpha())
print('Esse caracter é alfanúmerico? ', algo.isalnum())
print('Esse caracter está em maíusculo? ', algo.isupper())
print('Esse caracter está em minúsculo? ', algo.islower())
print('Esse caracter está em captalizado (maiúsculo e minúsculo)? ', algo.istitle())
print('Esse caracter é formado somente de espaços?', algo.isspace())