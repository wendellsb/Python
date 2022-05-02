from curses.ascii import isspace


x = input('Digite algo: ')

print('O tipo primitivo desse valor é: ', type(x))
print('Tem espaços? ', x.isspace())
print('É um numero? ', x.isnumeric())
print('É alfabetico? ', x.isalpha())
print('É alfanumerico? ', x.isalnum())
print('Está em maiúscula? ', x.isupper())
print('Está em minuscula? ', x.islower())

