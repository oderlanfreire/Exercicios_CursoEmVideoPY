from datetime import date

anoAt = date.today().year

nasc = int(input("Insira o ano de nascimento do atleta: "))

idade = anoAt - nasc

if idade < 0:
    print("Ano de nascimento inválido, por favor insira o ano certo!")
    nasc = int(input("Insira o ano de nascimento do atleta: "))
    idade = anoAt - nasc


if idade < 10:
    print("O atleta tem {} anos.\nCategoria: MIRIM" .format(idade))
elif idade >= 10 and idade < 15:
    print("O atleta tem {} anos.\nCategoria: INFANTIL" .format(idade))
elif idade >= 15 and idade < 20:
    print("O atleta tem {} anos.\nCategoria: JÚNIOR" .format(idade))
elif idade >= 20 and idade <= 25:
    print("O atleta tem {} anos.\nCategoria: SÊNIOR" .format(idade))
else:
    print("O atleta tem {} anos.\nCategoria: MASTER" .format(idade))
