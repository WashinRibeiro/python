# 7. Desenvolva um programa que leia as duas notas do aluno,
# calcule e mostre a sua média

n1 = float(input('Entre com a valor da primeira nota: '))
n2 = float(input('Entre com o valor da segunta nota: '))
media = (n1 + n2) / 2

print('Com a primeira nota sendo {} e a segunda nota {}, '
      'o aluno ficou com a média de {:.2f}'.format(n1, n2, media))