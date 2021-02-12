# 10. Crie um programa que leia quanto dinheiro uma pessoa
# tem na carteira e mostre quantos dólares ela pode comprar
# $1Dólar = R$5,35

real = float(input('Quantos reais você tem na carteira? '))
print('Com {} reais, você conseguiria comprar {:.2f} dólares'.format(real, real/5.35))
