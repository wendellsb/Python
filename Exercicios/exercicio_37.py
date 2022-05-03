n = int(input('Informe um numero: '))
print('Informe a basede converção')
print('[ 1 ] para Binario')
print('[ 2 ] para Octal')
print('[ 3 ] para Hexadecimal')
b = int(input('Qual a base? '))

if b == 1 :
    print('{} convertido para Binário é igual a {}'.format(n, bin(n)))
elif b == 2 :
    print('{} convertido para Octal é igual a {}'.format(n, oct(n)))
elif b == 3 :
    print('{} convertido para Hexadecimal é igual a {:.2f}'.format(n, hex(n)))
else :
    print('Base não encontrada!')