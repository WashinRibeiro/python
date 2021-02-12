# 12. Faça um algorítmo que leia o preço de um produto
# e mostre seu novo preço com 5% de desconto

valor = float(input('Qual o valor do produto? '))
print('Com desconto de 5%, esse produto de R${:.2f} '
      'valerá R${:.2f}'.format(valor, valor*0.95))
