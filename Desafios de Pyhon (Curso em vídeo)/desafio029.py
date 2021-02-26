# 29 - Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo
# que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

vel = float(input('Entre com a velocidade do carro: '))

if (vel > 80):
    print('VOCÊ FOI MULTADO POR ESTAR {:.2f}KM ACIMA DO LIMITE!!!'.format(vel - 80))
    print('Terá que pagar um valor de R${:.2f}'.format(7.00*(vel - 80)))
else:
    print('Tudo certo!! Ande com atenção')