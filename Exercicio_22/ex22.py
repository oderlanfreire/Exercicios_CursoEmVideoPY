name = str(input("Insira seu nome completo: ")).strip()

print('Nome em maiusculo: {}' .format(name.upper()))
print('Nome em minusculo: {}' .format(name.lower()))
print("A quantidade de caracteres do seu nome é {}" .format(
    len(name)-name.count(" ")))
print("O seu primeiro nome tem {} quantidades de caracteres" .format(name.find(' ')))
