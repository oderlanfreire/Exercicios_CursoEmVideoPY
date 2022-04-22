num = int(input("Insira um número: "))
count = 0

for x in range (1, num +1):
    if num % x == 0:
        count = count +1

if count > 2:
    print("O número {} não é primo pois foi dividido {} vezes no intervalo de 1 a {}" .format(num, count, num))
elif count == 2:
    print("O número {} é primo, só foi dividido {} vezes, por 1 e por ele mesmo no intervalo entre 1 e {}" .format(num, count, num))