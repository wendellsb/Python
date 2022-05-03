import random
numero = int(input('Informe um numero de 1 a 5: '))
aleatorio = random.randint(1,5)

if aleatorio == numero :
    print('Venceu!')
else :
    print('Perdeu!')
    
print('O numero pensado foi {}'.format(aleatorio))