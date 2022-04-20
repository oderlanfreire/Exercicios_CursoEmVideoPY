from time import sleep


print("Calculando o IMC")
peso = float(input("Insira seu peso em KG: "))
altura = float(input("Insira a sua altura em metros: "))

imc = peso/altura**2

print("Calculando...")
sleep(2)
if imc < 18.5:
    print("Seu IMC é de {:.2f}, está abaixo do ideal!" .format(imc))
elif imc >= 18.5 and imc <= 25:
    print(
        "Seu IMC é de {:.2f}, considerado o ideal para sua altura e peso!" .format(imc))
elif imc > 25 and imc <= 30:
    print("Seu IMC é de {:.2f}, você esta com sobrepeso!" .format(imc))
elif imc > 30 and imc <= 40:
    print(
        "Seu IMC é de {:.2f}, você esta em um quadro de obesidade!" .format(imc))
else:
    print(
        "Seu IMC é de {:.2f}, você se encontra em um quadro de obesidade morbida!" .format(imc))
