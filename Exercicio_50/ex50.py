soma = 0
print("Informe 6 numeros, um de cada vez quando pedido")

for x in range(1, 7):
    num = int(input("Insira um numero e aperte enter: "))
    if num % 2 == 0:
        soma = soma + num

print("A soma de todos os numeros pares que você informou é: ", soma)