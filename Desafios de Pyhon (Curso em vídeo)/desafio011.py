# 11. Faça um programa que leia a largura e altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta pinta uma área de 2m²

alt = float(input('Entre com o valor da altura dessa parede: '))
larg = float(input('Entre com o valor da largura dessa parede: '))

print('Com uma parede que possuí {}m de altura e'
      ' {}m de largura, você pecisará de {:.2f} litros '
      'de tinta'.format(alt, larg, (alt * larg)/2))
