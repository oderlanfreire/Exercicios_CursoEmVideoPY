
sexo = str(input("Informe seu sexo[M/F]: ")).strip().upper()[0]
while sexo not in 'M F':
    sexo = str(input("Imformação invalida, Informe seu sexo[M/F]: ")).strip().upper()[0]
print("Fim")