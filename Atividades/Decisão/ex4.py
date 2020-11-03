#Faça um programa para ler o ano de nascimento de uma pessoa e escrever uma mensagem que diga se ela poderá ou não votar este ano (não é necessário considerar o mês em que ela nasceu)

ano_nascimento = int(input("Digite o seu ano de nascimento: "))

idade = 2020 - ano_nascimento

if idade > 18:
  print('VOCÊ PODERÁ VOTAR')
else:
  print('VOCÊ AINDA É MENOR DE IDADE E NÃO PODE VOTAR')