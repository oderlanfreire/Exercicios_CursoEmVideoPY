from random import randint

print("Vamos jogar? Advinhe qual número eu pensei entre 1 e 10")

compJogada = randint(1, 10)
persJogada = int(input("Insira sua jogada: "))
jogadaInvalida = 0

if persJogada > 10:
    print("Número escolhido inválido, tente de novo")
    jogadaInvalida += 1
    persJogada = int(input("Insira sua jogada: "))

cont = 1

while compJogada != persJogada:
    if persJogada > 10:
        print("Número invalido, tente de novo")
        jogadaInvalida += 1
        persJogada = int(input("Insira sua jogada: "))
    else:
        print("Errou, tente de novo")
        persJogada = int(input("Insira sua jogada: "))
        cont += 1

if compJogada == persJogada:
    print("Parabéns você acertou, o numero escolhido pela maquina é {}!\nVocê venceu com {} jogadas válidas!\nE {} jogadas inválidas!\nSeu total de jogadas foi {}!" .format(compJogada, cont, jogadaInvalida, cont + jogadaInvalida))