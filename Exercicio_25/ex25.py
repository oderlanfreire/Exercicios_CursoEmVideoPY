nome = str(input("Insira o nome completo: ")).strip()
busca = str(input("Insira o nome que quer verificar: ")).strip()

contem = False

if(nome[:len(nome)].lower().__contains__(busca.lower())):
    contem = True

print(contem)
