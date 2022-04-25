
maiorIdadeH = 0;
nomeMIdadeH = ""
idadeTotal = 0
contF = 0

for x in range (1, 5):
    print("======== {} PESSOA ========" .format(x))
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo[M/F]: ")).strip().upper()
    
    idadeTotal = idade

    if sexo == "M":
        if idade > maiorIdadeH:
            maiorIdadeH = idade
            nomeMIdadeH = nome
    elif sexo == "F":
        if idade < 20:
            contF += 1
    

print("A idade média do grupo é de {:.1f} anos." .format(idadeTotal/4))
print("O homem mais velho do grupo é {} com {} anos de idade." .format(nomeMIdadeH.upper(), maiorIdadeH))
print("Existe um total de {} mulheres com menos de 20 anos de idade nesse grupo." .format(contF))