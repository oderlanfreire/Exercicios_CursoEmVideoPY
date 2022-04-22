print("---------Bem vindo a loja--------")
compras = float(input("Preço das compras: R$"))
pagamento = int(input('''Qual o metodo de pagamento?
[1] à vista no dinheiro\cheque
[2] à vista no cartão
[3] parcelado 2x no cartão
[4] 3 ou mais vezes no cartão
Qual é a opção? '''))


if pagamento == 1:
    pFinal = compras - (compras*(10/100))
    print("Sua compra é de R${:.2f}, vai custar R${:.2f} no final." .format(compras, pFinal))
elif pagamento == 2:
    pFinal = compras - (compras*(5/100))
    print("Sua compra é de R${:.2f}, vai custar R${:.2f} no final." .format(compras, pFinal))
elif pagamento == 3:
    print("Você vai pagar R${:.2f}, nessa modalidade de pagamento não há descontos ou juros!" .format(compras))
elif pagamento == 4:
    nParc = int(input("Qual o número de parcelas? "))
    pFinal = compras + (compras*(20/100))
    pParc = pFinal/nParc
    print("Sua compra é parcelada em {}x de R${:.2f} com juros aplicado.\nA sua compra de R${:.2f} vai custar R${:.2f} no final." .format(nParc, pParc, compras, pFinal))
else:
    print("Opção inválida!, refaça todo o processo!")