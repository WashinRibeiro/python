# 14. Escreva um programa que converta uma temperatura digitando
# em graus Celsius e converta para graus Fahrenheit.

c = float(input('Quantos °C está nesse momento? '))
f = ((9*c)/5) + 32
k = c + 273.15
print('{}°C equivale a {}°F e a {:.2f}K'.format(c, f, k))
