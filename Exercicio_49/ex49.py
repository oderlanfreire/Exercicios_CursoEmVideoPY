print("{:=^30}" .format("TABUADA"))

num = int((input("Insira um numero para ver sua tabuada: ")))

for i in range(1, 11):
    print("{} x {} = {}". format(num, i, num*i))