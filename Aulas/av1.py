# -*- coding: utf-8
# Wendell
'''
Escreva um programa para calcular a redução do tempo de vida de um fumante.
Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou.
Considere que um fumante perde 10 minutos de vida a cada cigarro, calcule quantos 
dias de vida um fumante perderá. Exiba o total de dias'''
#1

cigarros=(int(input('Quantos cigarros por dia você já fumou?  ')))
print(cigarros)

anos=(int(input('Quantos anos você fuma?  ')))
print(anos)

dias=anos*365
total_cigarros=cigarros*dias
minutos=1440

print(f'Voce fumou {total_cigarros}')
tempo_perdido=total_cigarros*10
print(tempo_perdido)

resposta=round(tempo_perdido/minutos)
print(f'Dias perdidos foram: {resposta}')

#2
'''
Uma academia deseja fazer um censo entre seus clientes para descobrir o 
mais alto, o mais baixo, a mais gordo e o mais magro, para isto você deve 
fazer um programa que pergunte a cada um dos clientes da academia seu código, 
sua altura e seu peso. O final da digitação de dados deve ser dada quando o 
usuário digitar 0 (zero) no campo código. Ao encerrar o programa também deve ser 
informados os códigos e valores do cliente mais alto, do mais baixo, do mais gordo 
e do mais magro, além da média das alturas e dos pesos dos clientes
'''
'''
mais_alto=0
mais_baixo=999
mais_gordo=0
mais_magro=999
saida = 1
while saida !=0:
    cod=(int(input('Informe seu codigo: ')))
    print('Codigo: ',cod)

    alt=(int(intput('Informe sua altura: ')))
    print('Codigo: ',alt)
    if alt > mais_alto:
        mais_alto = alt
        cod_alto = cod
    if alt < mais_baixo:
        mais_alto = alt
        cod_baixo = cod

    peso=(int(intput('Informe seu peso: ')))
    print('Codigo: ',peso)
    if peso > mais_gordo:
        mais_gordo = peso
        cod_gordo = peso
    if peso < mais_magro:
        mais_magro = peso
        cod_magro = peso

    soma_altura= soma_altura + alt
    soma_peso= soma_peso + peso
    contador = contador + 1

    saida=(int(input('Para finalizar digite: 0')))
   

media_altura=soma_altura/contador
media_peso=soma_peso/contador
print(f"O codigo do mais alto {cod_alto} e a altura é {mais_alto}!")
print(f"O codigo do mais baixo {cod_baixo} e a altura é {mais_baixo}!")
print(f"O codigo do mais gordo {cod_gordo} e peso é {mais_gordo}!")
print(f"O codigo do mais magro {cod_magro} e peso é {mais_magro}!")
print(f"A media de altura {media_altura}!")
print(f"A media de peso {media_peso}!")
'''
#3
'''
Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" 
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa 
responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice"
 e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
'''
#[]
'''
lista=["Telefonou para a vítima?", "Esteve no local do crime?", "Mora perto da vítima?", "Devia para a vítima?", "Já trabalhou com a vítima?"]
print(lista)

resposta=(int(input('Quantas perguntas dessas você diria sim? ')))
if resposta == 2:
    print('Suspeita')
elif resposta == 3 or resposta == 4:
    print('Cúmplice')
elif resposta == 5:
    print('Assassino')
else:
    print('Inocente')
'''

#4
'''
Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única 
que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares.
'''
'''
lista= [[], []]
for i in range(0, 7):
    aux=(int(input('Informe um numero: ')))
    if aux % 2 == 0:
        lista[0].append(aux)
    else :
        lista[1].append(aux)
print(lista)

nova_lista = lista[0] + lista[1]
print(nova_lista)
'''