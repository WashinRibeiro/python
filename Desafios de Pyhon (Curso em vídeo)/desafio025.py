# 25 - Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

nome = str(input('Escreva seu nome: ')).strip()
print('Esse usuário tem SILVA no nome: {}'.format('silva' in nome.lower()))