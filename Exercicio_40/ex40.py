print("Insira as notas do aluno")
n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))
n3 = float(input("Terceira nota: "))


media = (n1 + n2+ n3)/3

if media > 6.9 and media <= 10:
    print("Tirando as notas {}, {} e {}, a média do aluno é {:.2f}." .format(n1, n2, n3, media))
    print("O aluno está APROVADO!")
elif media > 3.9 and media < 7:
    print("Tirando as notas {}, {} e {}, a média do aluno é {:.2f}." .format(n1, n2, n3, media))
    print("O aluno está de RECUPERAÇÃO!")
else:
    print("Tirando as notas {}, {} e {}, a média do aluno é {:.2f}.".format(n1, n2, n3, media))
    print("O aluno está REPROVADO!")