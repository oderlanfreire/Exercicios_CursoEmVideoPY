from ntpath import join


frase = str(input("Insira sua frase: ")).strip().lower()
frase2 = frase.split()
juntar = "".join(frase2)
inverso = juntar[::-1]


if juntar == inverso:
    print("a frase {} é um palindromo, pois seu inverso é {}!" .format(juntar, inverso))
else:
    print("as frases {} e {} são diferentes, ou seja, não é um palindromo!" .format(juntar, inverso))