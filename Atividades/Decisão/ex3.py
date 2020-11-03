#Faça um programa para entrar com um número e dizer se o mesmo é par ou ímpar.

num = int(input("Entre com um numero: "))

resto = num % 2

if resto == 0:
  print("PAR")
else:
  print("IMPAR")