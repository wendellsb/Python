from tkinter import N


soma = 0
for i in range(0, 6) :
    n = int(input('Numero: '))
    if n%2 == 0 :
        soma += n
print(soma)
        