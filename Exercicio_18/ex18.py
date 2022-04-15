import math

angulo = float(input("Insira o angulo que você deseja: "))

seno = math.sin(math.radians(angulo))
coss = math.cos(math.radians(angulo))
tang = math.tan(math.radians(angulo))

print("O seno, cosseno e tangente do angulo de {:.1f} são:\nSENO = {:.2f}\nCOS = {:.2f}\nTAN = {:.2f}" .format(
    angulo, seno, coss, tang))
