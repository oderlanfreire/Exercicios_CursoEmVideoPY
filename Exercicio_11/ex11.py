baseParede = float(input("Largura da parede em metros: "))
alturaParede = float(input("Altura da parede em metros: "))

area = baseParede*alturaParede
tinta = area/2

print('Sua parede tem dimensão {}x{} e sua área é  de {}m².\nPara pintar essa parede, sera necessário {} litros de tinta.' .format(
    baseParede, alturaParede, area, tinta))
