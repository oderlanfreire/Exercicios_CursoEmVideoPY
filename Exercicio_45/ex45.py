import random
from time import sleep
print("{:=^40}" .format("JOKENPO"))

maquina = random.randint(0,2)

escolha = int(input('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA
Qual sua escolha? '''))

if(escolha < 0 or escolha > 2):
    print("Escolha invalida, refaça o processo!")
    exit()

sleep(1)
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!")

if maquina == 0:
    print("=-=-=-=-=-=-=-=-=-=-=")
    print("O computador jogou pedra")
    if escolha == 0:
        print("O jogador jogou pedra")
        print("=-=-=-=-=-=-=-=-=-=-=")
        print("EMPATE!")
    elif escolha == 1:
        print("O jogador jogou papel")
        print("=-=-=-=-=-=-=-=-=-=-=")
        print("O JOGADOR VENCEU!")
    else:
        print("O jogador jogou tesoura")
        print("=-=-=-=-=-=-=-=-=-=-=")
        print("O COMPUTADOR VENCEU!")
elif maquina == 1:
    print("=-=-=-=-=-=-=-=-=-=-=")
    print("O computador jogou papel")
    if escolha == 0:
        print("O jogador jogou pedra")
        print("=-=-=-=-=-=-=-=-=-=-=")
        print("O COMPUTADOR VENCEU!")
    elif escolha == 1:
        print("O jogador jogou papel")
        print("=-=-=-=-=-=-=-=-=-=-=")
        print("EMPATE!")
    else:
        print("O jogador jogou tesoura")
        print("=-=-=-=-=-=-=-=-=-=-=")
        print("O JOGADOR VENCEU!")
elif maquina == 2:
    print("=-=-=-=-=-=-=-=-=-=-=")
    print("O computador jogou tesoura")
    if escolha == 0:
        print("O jogador jogou pedra")
        print("=-=-=-=-=-=-=-=-=-=-=")
        print("O JOGADOR VENCEU!")
    elif escolha == 1:
        print("O jogador jogou papel")
        print("=-=-=-=-=-=-=-=-=-=-=")
        print("O COMPUTADOR VENCEU!")
    else:
        print("O jogador jogou tesoura")
        print("=-=-=-=-=-=-=-=-=-=-=")
        print("EMPATE!")