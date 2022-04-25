from datetime import date, datetime

maior = 0;
menor = 0;

for x in range(1, 8):
    ano = int(input("Insira o ano de nascimento da {}º pessoa: " .format(x)))
    anoAt = date.today().year
    idade = anoAt - ano
    if idade >= 18:
        maior += 1
    elif idade < 18:
        menor += 1
    else:
        print("Ano de nascimento invalido, reinicie todo o processo!")
        exit()

print("O número de  maiores de idade é {}.\nO número de menores de idade é {}." .format(maior, menor))