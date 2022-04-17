print('-------Radar------')
vel = float(input("Qual a velocidade que o radar registrou? "))
if(vel > 80):
    print("Você ultrapassou o limite de velocidade de 80KM/h!\nSua Velocidade: {}KM/h".format(vel))
    print("Sua multa é de: R${:.2f}" .format((vel - 80) * 7.0))
