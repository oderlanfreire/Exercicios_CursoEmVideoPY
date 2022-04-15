from audioop import alaw2lin
import random

al1 = str(input("Primeiro aluno: "))
al2 = str(input("Segundo aluno: "))
al3 = str(input("Terceiro aluno: "))
al4 = str(input("Quarto aluno: "))

listaA = [al1, al2, al3, al4]

random.shuffle(listaA)
print("A ordem de apresentação de trabalho é a dos seguintes alunos {}" .format(listaA))
