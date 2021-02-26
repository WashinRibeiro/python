# 27 - Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente

nome = str(input('Entre com o seu nome: ')).strip().split()
print('Seu primeiro nome é: {}'.format(nome[0]))
print('Seu último nome é: {}'.format(nome[len(nome)-1])) 

#Com o len() conseguimos ver o total de partes que o 
#nome possuí e então com o -1 vemos o último