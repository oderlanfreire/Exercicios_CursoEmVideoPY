print("Considere o Dólar igual a RS4.70, Euro igual a 5.08, iene japones R$ 0.037")
dinheiro = float(input("Quanto dinheiro você tem na carteira? R$"))
dolarconv = dinheiro/4.7
euroconv = dinheiro/5.08
ieneconv = dinheiro/0.037

print("Com R${:.2f} você pode comprar US${:.2f} ou €{:.2f} ou ¥{:.2f}" .format(
    dinheiro, dolarconv, euroconv, ieneconv))
