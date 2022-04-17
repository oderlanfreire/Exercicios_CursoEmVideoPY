from pickle import FALSE, TRUE


cidade = str(input("Insira o nome de uma cidade: ")).strip()

santo = False

if(cidade[:5].lower() == "santo"):
    santo = True
elif(cidade[:3].lower() == "são"):
    santo = True
elif(cidade[:3].lower() == "sao"):
    santo = True

print("Sua cidade recebe nome de santo? ", santo)
