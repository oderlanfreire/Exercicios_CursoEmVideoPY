print("{:=^30}" .format(" OS 10 PRIMEIROS TERMOS DE UMA P.A "))

termo = int(input("Insira o valor do primeiro termo: "))
razao = int(input("Insira a razão: "))

for i in range(1, 11):
    if i < 10:
        print(termo, " →", end=" ")
    else:
        print(termo)
    termo = termo + razao