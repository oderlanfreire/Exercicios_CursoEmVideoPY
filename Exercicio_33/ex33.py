val1 = int(input("Digite o primeiro número: "))
val2 = int(input("Digite o segundo número: "))
val3 = int(input("Digite o terceiro número: "))

if(val1 > val2 and val1 > val3):
    print("O maior número é o: {}" .format(val1))
elif(val2 > val1 and val2 > val3):
    print("O maior número é o: {}" .format(val2))
else:
    print("O maior número é o: {}".format(val3))


if(val1 < val2 and val1 < val3):
    print("O menor número é: {}" .format(val1))
elif(val2 < val1 and val2 < val3):
    print("O menor número é o: {}" .format(val2))
else:
    print("O menor número é o: {}" .format(val3))
