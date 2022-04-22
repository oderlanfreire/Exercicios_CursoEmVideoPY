soma = 0;

for x in range(1, 501, 2):
    if x % 3 == 0 and x % 2 != 0:
        soma = soma + x;

print("A soma dos valores impares divisiveis por 3 de 1 a 500 é: {}." .format(soma))