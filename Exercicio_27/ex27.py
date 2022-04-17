nome = str(input("Insira o nome completo: ")).strip()
fname = nome.split()

print("Seu primeiro nome é: {}\nJá seu último nome é: {}" .format(
    fname[0], fname[len(fname)-1]))
