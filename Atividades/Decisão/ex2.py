#Faça um programa para entrar com uma distância (Km), o tempo de viagem (Horas) e dizer se a velocidade média foi superior ao limite (80 Km/h) ou não.

km = float(input('Digite os km percorridos: '))
horas = float(input('Digite o tempo de viagem em horas: '))

velocidade = km / horas

print('{:.2f} km/hora'.format(velocidade))

if velocidade > 80:
   print('Velocidade superior ao limite')
else: 
  print('Velocidade normal')