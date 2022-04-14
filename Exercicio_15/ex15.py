diasAlugado = int(input("Por quantos dias o carro foi alugado? "))
km = float(input("Quantos Km o carro percorreu? "))

ValTotD = diasAlugado * 60
ValTotKM = km * 0.15

print("O valor total em Reais por {} dias de aluguel do carro é de R${}.\nO valor pela quantidade de {} KM percorrido é de R${}.\nNo total você pagará: R${}" .format(
    diasAlugado, ValTotD, km, ValTotKM, ValTotD + ValTotKM))
