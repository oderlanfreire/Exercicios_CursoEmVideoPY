print("Considere o Dólar com valor igual a 4.70")
dinheiro = float(input("Quanto dinheiro você tem na carteira? R$"))
dolarconv = dinheiro/4.7

print("Com R${:.2f} você pode comprar US${:.2f}" .format(dinheiro, dolarconv))
