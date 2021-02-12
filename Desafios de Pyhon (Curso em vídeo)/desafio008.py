# 8. Escreva um programa que leia um valor em metros
# e o exiba convertido em centímetros e milímetros

m = float(input('Digite o valor em metros: '))
print('A medida de {}m equivale a {:.2f}cm e a'
      ' {:.2f}mm'.format(m, m*100, m*1000))
