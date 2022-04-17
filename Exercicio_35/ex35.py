A = float(input("Insira o primeiro seguimento: "))
B = float(input("Insira o segundo seguimento: "))
C = float(input("Insira o terceiro seguimento: "))

if(A < B + C and B < A + C and C < A + B):
    print("Os valores podem formar um triângulo!")
else:
    print("Os valores não conseguem formar um triângulo!")