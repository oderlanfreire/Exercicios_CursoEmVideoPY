val = float(input("Quanto você recebe de salário? "))

if(val > 1250):
    print("Seu novo salário é de: R${:.2f}" .format(val + (val*(10/100))))
else:
    print("Seu novo salário é de: R${:.2f}" .format(val + (val*(15/100))))
