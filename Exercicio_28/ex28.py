import random

comp = random.randint(0, 5)
print("---------- Jogo da Advinhação ----------")
print("Escolha um numero entre 0 e 5, se seu número for o mesmo que o computador você ganha, se for diferente você perde")
user = int(input("Insira sua aposta: "))
if(comp == user):
    print("Parabéns, você ganhou!")
    print("Sua aposta: {}\nAposta da máquina: {}".format(user, comp))
else:
    print("A maquina ganhou!")
    print("Sua aposta: {}\nAposta da máquina: {}" .format(user, comp))
