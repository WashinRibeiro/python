#Faça um programa para ler a temperatura de uma pessoa e exibir a mensagem "ESTÁ COM FEBRE" ou "ESTÁ NORMAL". Considere o valor base como 36.5

temp = float(input('Qual é a sua temperatura: '))

if temp > 36.5:
  print('Você está com febre')
elif temp < 35:
  print('Sua temperatura está baixa')
else: 
  print('Temperatura Normal') 
