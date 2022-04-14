salario = float(input("Insira o valor do seu salario: "))
porcentagem = float(input("Insira a porcentagem de aumento: "))

novoSalario = salario + (salario * (porcentagem/100))
print("O seu salario antigo que era de R${:.2f}, ganhou {:.0f}% de aumento, seu novo salário é de R${:.2f}" .format(
    salario, porcentagem, novoSalario))
