frase = str(input("Insira a Frase: ")).strip()
buscar = str(input("Insira a letra para a busca: ")).strip()

print("A letra {} aparece {} vezes, sendo a primeira vez na posição {} e sua ultima aparição foi na posição {}".format(
    buscar.lower(), frase.lower().count(buscar.lower()), frase.lower().find(buscar.lower())+1, frase.lower().rfind(buscar.lower())+1))
