numeros = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros :
        numeros.append(n)
        print('Valor adicionado')        
    else :
        print('Valor duplicado não vou adicionar!')
    resposta = input('Deseja continuar? [S/N] ')
    if resposta in 'Nn' :
        break

print('-=' * 30)
numeros.sort()
print(f'Você digitou os valores {numeros} ')