valor = int(input('Insira um numero para calcular sua tabuáda: '))
print('-----------')
for x in range(1, 10):
    mult = valor * x
    print('{} x {} = {}'.format(valor, x, mult))
print('-----------')
