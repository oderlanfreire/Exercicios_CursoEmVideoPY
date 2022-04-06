num = int(input("Insira um número: "))
dobro = num * 2
triplo = num * 3
raiz = num ** (1/2)
print("O dobro de {num} é: {dobro}\nO triplo de {num} é: {triplo}\nA raiz quadrada de {num} é: {raiz:.2f}".format(
    num=num, dobro=dobro, triplo=triplo, raiz=raiz))
