num = int(input("Insira um numero: "))
op = int(input(
    "Qual conversão você deseja realizar:\n[1] para binario.\n[2] para octal.\n[3] para hexadecimal.\nDigite o número da operação: "))
print("\n")
if op == 1:
    print("O número {} em binario é: {}" .format(num, bin(num)[2:]))
elif op == 2:
    print("O número {} em octal é: {}" .format(num, oct(num)[2:]))
elif op == 3:
    print("O número {} em hexadecimal é: {}" .format(num, hex(num)[2:]))
else:
    print("Opção inválida!")
