import random
aluno_1 = str(input("Primeiro aluno: "))
aluno_2 = str(input("Segundo aluno: "))
aluno_3 = str(input("Terceiro aluno: "))
aluno_4 = str(input("Quarto aluno: "))

sorteio = [aluno_1, aluno_2, aluno_3, aluno_4]


print("O aluno que deve apagar o quadro é {}, o mesmo foi escolhido em sorteio" .format(
    random.choice(sorteio)))
