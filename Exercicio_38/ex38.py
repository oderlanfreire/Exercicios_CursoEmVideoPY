print("Qual verificação de números")
n1 =  int(input("Insira o primeiro número: "))
n2 = int(input("Insira o sugundo número: "))

if n1 > n2:
    print("O primeiro número é maior!")
elif n2 > n1:
    print("O segundo número é maior!")
elif n1 == n2:
    print("Ambos tem o mesmo valor!")