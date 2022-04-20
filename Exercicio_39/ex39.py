from datetime import date, datetime
print("Alistamento Militar")
anoNasc = int(input("Insira o ano do seu nascimento: "))

anoAt = date.today().year
idade = anoAt - anoNasc

if(idade == 18):
    print("O jovem tem {} anos em {}.\nÉ hora de se alistar no serviço militar!" .format(
        idade, anoAt))
elif(idade < 18):
    print("o jovem tem {} anos em {}.\nAinda não é hora, faltam {} anos para que você possa se alistar!" .format(
        idade, anoAt, 18 - idade))
elif(idade > 18):
    print("o jovem tem {} anos em {}.\nDeveria ter se alistado no ano de {}.\nJa passou {} anos do seu período de alistamento!" .format(
        idade, anoAt, anoNasc + 18, idade - 18))
