maior = 0.0
menor = 0.0
pessoaMaior = 0
pessoaMenor = 0
for x in range(1, 6):
    peso = float(input("Insira o peso da {}ª pessoa: " .format(x)))
    if x == 1:
        maior = peso
        menor = peso
        
    if peso > maior:
        maior = peso
        pessoaMaior = x
    if peso < menor:
        menor = peso
        pessoaMenor = x

print("O maior peso é {:.2f}, pertencendo a {}ª pessoa!" .format(maior, pessoaMaior))
print("O menor peso é {:.2f}, pertencendo a {}ª pessoa!" .format(menor, pessoaMenor))