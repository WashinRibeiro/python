linha1 = input().split()
cod1 = int(linha1[0])
qtd1 = int(linha1[1])
valor1 = float(linha1[2])

linha2 = input().split()
cod2 = int(linha2[0])
qtd2 = int(linha2[1])
valor2 = float(linha2[2])

valorTotal = qtd1*valor1 + qtd2*valor2

print("VALOR A PAGAR: R$ {:.2f}".format(valorTotal))


