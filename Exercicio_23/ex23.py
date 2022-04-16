num = int(input("Insira um numero de 4 digitos: "))


print("Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}".format(
    num//1 % 10, num//10 % 10, num//100 % 10, num//1000 % 10))
