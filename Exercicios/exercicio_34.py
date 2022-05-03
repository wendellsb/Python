salario = float(input('Salario atual: '))
if salario > 1250.00 :
    salario *= 1.10
    print('Salario com aumento de 10%: ', salario)
else :
    salario *= 1.15
    print('Salario com aumento de 15%: ', salario)