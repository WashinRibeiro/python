# 31 - Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km
# para viagens de até 200Km e R$0,45 parta viagens mais longas.

print('VALORES DE VIAGEM')
print('-' * 30)

km = float(input('Quantos km de distância serão percorridos? '))
passagem = 0.5 * km

if(km > 200):
    print('Cada km corresponde a R$0,45... Então você pagará R${:.2f}'.format(0.45 * km))
else:
    print('Cada km corresponde a R$0,50... Então você pagará R${:.2f}'.format(0.5 * km))
