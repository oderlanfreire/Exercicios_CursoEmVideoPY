km = int(input("A viagem é de quantos KMs? "))

if(km <= 200):
    print("A sua passagem custa: R$ {:.2f}" .format(km*0.5))
else:
    print("A sua passagem custa: R$ {:.2f}" .format(km*0.45))
