produto = float(input("Insira o valor do produto: R$"))
promo = float(
    input("Qual a porcentagem de desconto?(Insira apenas o valor): "))

promocao = produto - (produto * (promo/100))

print(
    'O produto na promoção com {:.0f}% de desconto sai por R${:.2f}' .format(promo, promocao))
