n1 = int(input('Numero 1: '))
n2 = int(input('Numero 2: '))
n3 = int(input('Numero 3: '))

if n1 > n2 and n2 > n3 :
    print('O maior é o ', n1)
elif n2 > n1 and n1 > n3 :
    print('O maior é o ', n2)
elif n3 > n2 and n2 > n1 :
    print('O maior é o ', n3)
    
if n1 < n2 and n2 < n3 :
    print('O menor é o ', n1)
elif n2 < n1 and n1 < n3 :
    print('O menor é o ', n2)
elif n3 < n2 and n2 < n1 :
    print('O menor é o ', n3)