print("{:=^30}" .format("CALCULADORA"))

print("Insira dois números e escolha o valor correspondente a operação: ")
n1 = int(input("Insira o primeiro número: "))
n2 = int(input("Insira o segundo número: "))

op = int(input('''Escolha a operação:
[1] Soma
[2] Subtração
[3] multiplicação
[4] divisão
[5] sair\n'''))

if op == 6:
    print("Operação inválida, escolha uma operação valida!")
    op = int(input('''Escolha uma nova operação:
[1] Soma
[2] Subtração
[3] multiplicação
[4] divisão
[5] sair\n'''))


while op !=5:
    if op > 5:
        print("Operação inválida, Escolha uma operação valida!")
        op = int(input('''Escolha uma nova operação:
[1] Soma
[2] Subtração
[3] multiplicação
[4] divisão
[5] sair\n'''))

    if op == 1:
        print("Soma: {} + {} = {}" .format(n1, n2, n1 + n2))
        op = int(input('''Escolha uma nova operação:
[1] Soma
[2] Subtração
[3] multiplicação
[4] divisão
[5] sair\n'''))
    elif op == 2:
        print("Subtração: {} - {} = {}" .format(n1, n2, n1 - n2))
        op = int(input('''Escolha uma nova operação:
[1] Soma
[2] Subtração
[3] multiplicação
[4] divisão
[5] sair\n'''))
    elif op == 3:
        print("Multiplicação: {} * {} = {}" .format(n1, n2, n1 * n2))
        op = int(input('''Escolha uma nova operação:
[1] Soma
[2] Subtração
[3] multiplicação
[4] divisão
[5] sair\n'''))
    elif op == 4:
        print("Divisão: {} / {} = {:.2f}" .format(n1, n2, n1/n2))
        op = int(input('''Escolha uma nova operação:
[1] Soma
[2] Subtração
[3] multiplicação
[4] divisão
[5] sair\n'''))

print("Você saiu do programa...")