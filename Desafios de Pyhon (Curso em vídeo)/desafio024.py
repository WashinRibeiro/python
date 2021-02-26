# 24 - Crie um programa que leia um nome de uma cidade
# e diga se ela começa ou não com o nome 'SANTO'

cidade = str(input('Digite o nome da sua cidade: ')).strip()
print('A cidade mencionada acima começa com a palavra "SANTO"')
print(cidade[:5].upper() == 'SANTO')