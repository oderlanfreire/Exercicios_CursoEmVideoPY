a = float(input("Insira o valor da primeira reta: "))
b = float(input("Insira o valor do segunda reta: "))
c = float(input("Insira o valor do terceira reta: "))

if a < (b + c) and b < (a + c) and c < (a + b):
    print("As retas {}, {} e {} podem formar um triangulo:" .format(a, b, c))

    if a == b and a == c:
        print("Equilátero")
    elif a == b and a != c or a == c and a != b or b == c and b != a:
        print("Isóceles")
    elif(a != b and a != c):
        print("escaleno")
else:
    print("Os as retas {}, {} e {} não conseguem formar um triângulo!" .format(a, b, c))
