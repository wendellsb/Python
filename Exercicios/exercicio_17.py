import math
co = float(input('Informe o cateto oposto: '))
ca = float(input('Informe o cateto adjacente: '))
hi = math.hypot(co, ca)

print('A Hipotenusa é: {:.2f}' .format(hi))