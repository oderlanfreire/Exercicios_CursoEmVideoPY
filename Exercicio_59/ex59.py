from time import sleep


print("{:=^30}" .format("CALCULADORA"))

print("Insira dois números e escolha o valor correspondente a operação: ")
n1 = int(input("Insira o primeiro número: "))
n2 = int(input("Insira o segundo número: "))

op = int(input('''Escolha a operação:
[1] Soma
[2] Multiplicação
[3] Maior
[4] Novos números
[5] sair\n'''))

if op == 6:
    print("Operação inválida, escolha uma operação valida!")
    sleep(1)
    op = int(input('''Escolha uma nova operação:
[1] Soma
[2] Multiplicação
[3] Maior
[4] Novos números
[5] sair\n'''))


while op !=5:
    if op > 5:
        print("Operação inválida, Escolha uma operação valida!")
        sleep(1)
        op = int(input('''Escolha uma nova operação:
[1] Soma
[2] Multiplicação
[3] Maior
[4] Novos números
[5] sair\n'''))

    if op == 1:
        print("Soma: {} + {} = {}" .format(n1, n2, n1 + n2))
        sleep(1)
        op = int(input('''Escolha uma nova operação:
[1] Soma
[2] Multiplicação
[3] Maior
[4] Novos números
[5] sair\n'''))
    elif op == 2:
        print("Multiplicação: {} * {} = {}" .format(n1, n2, n1 * n2))
        sleep(1)
        op = int(input('''Escolha uma nova operação:
[1] Soma
[2] Multiplicação
[3] Maior
[4] Novos números
[5] sair\n'''))
    elif op == 3:
        maior = n2
        if n1 > n2:
            maior = n1
        print("O maior numero entre {} e {} é {}!" .format(n1, n2, maior))
        sleep(1)
        op = int(input('''Escolha uma nova operação:
[1] Soma
[2] Multiplicação
[3] Maior
[4] Novos números
[5] sair\n'''))
    elif op == 4:
        n1 = int(input("Insira o novo valor para o primeiro numero: "))
        n2 = int(input("Insira o novo valor para o segundo número: "))
        sleep(1)
        op = int(input('''Escolha uma nova operação:
[1] Soma
[2] Multiplicação
[3] Maior
[4] Novos números
[5] sair\n'''))

sleep(1)
print("Você saiu do programa...")