import math

cateOposto = float(input("Insira o comprimento do cateto oposto: "))
cateAdj = float(input("Insira o comprimento do cateto adjacente: "))

print("A medida da hipotenusa é de {:.2f}".format(
    math.hypot(cateOposto, cateAdj)))
