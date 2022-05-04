valores = []
for cont in range(0, 5) :
    valores.append(int(input('Digite um valor: ')))

maximo = max(valores)
minimo = min(valores)
print(f"Você digitou os valores {valores}")
print(f'O maior valor digitado foi {maximo} na posição {valores.index(maximo)} ')
print(f'O menor valor digitado foi {minimo} na posição {valores.index(minimo)} ')