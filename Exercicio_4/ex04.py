obj = input('Digite o que você quiser: ')

print('Qual tipo primitivo do que você digitou?', type(obj))
print('É alfabetico? ', obj.isalpha())
print('É um numero? ', obj.isnumeric())
print('É apenas espaço? ', obj.isspace())
print('Tem valores ASCII? ', obj.isascii())
print('É digito? ', obj.isdigit())
print('É inteiro maiusculo? ', obj.isupper())
print('É inteiro minúsculo? ', obj.islower())
print('É decimal? ', obj.isdecimal())