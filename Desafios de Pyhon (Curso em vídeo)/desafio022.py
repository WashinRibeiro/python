# 22 - Crie um programa que leia o nome completo de uma pessoa e mostre:
# --> O nome com todas letras maíusculas
# --> O nome com todas letras minúsculas
# --> Quantas letras tem sem contar o espaço
# --> Quantas letras tem o primeiro nome

nome = input('Entre com seu nome: ').strip() #para retirar os espaços antes e depois do nome
print('Analisando seu nome...')
dividido = nome.split()
#nome_sem_espaço = ''.join(dividido)

print('Seu nome em maiúsculo é: {}'.format(nome.upper()))
print('Seu nome em minúsculo é: {}'.format(nome.lower()))
print('Seu nome possuí {} letras'.format(len(nome) - nome.count(' ')))
# ou print('Seu nome tem ao todo {}'.format(len(nome_sem_espaço)))
print('Seu primeiro nome tem {} letras'.format(len(dividido[0])))
# ou print('Seu primeiro nome possuí {} letras'.format(len(dividido[0])))