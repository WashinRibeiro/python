# 13. Faça um algoritmo que leia o salário de um funcionário
# e mostre seu novo salário com 15% de desconto

sal = float(input('Qual o valor do seu salário? '))
print('Ao descontar 15% do seu salário de R${:.2f},'
      ' você receberá {:.2f}'.format(sal, sal*0.85))
