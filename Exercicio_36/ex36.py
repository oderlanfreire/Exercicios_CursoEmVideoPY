from time import sleep


vCasa = float(input("Qual o valor da casa? R$"))
salario = float(input("Quanto você recebe? R$"))
pTempo = int(input("Em quanto tempo em anos você quer pagar? "))

prestacao = vCasa/(pTempo*12)

print("\nCALCULANDO...\n")

sleep(3)

if(prestacao > (salario*(30/100))):
    print("NEGADO! O valor da prestação de uma casa de R${} em {} anos é de R${:.2f}, execendo o valor máximo estipulado de 30% do seu salário!" .format(
        vCasa, pTempo, prestacao))
elif(prestacao < (salario*(30/100))):
    print("APROVADO! O valor da prestação de uma casa de R${} em {} anos é de R${:.2f}, esse valor está dentro do percentual estimado de 30% do seu salário, vamos fechar um contrato?!" .format(vCasa, pTempo, prestacao))
