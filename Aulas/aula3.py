#  -*- coding: utf-8 -*-

#manipulando cadeias de caracteres - strings
texto=('Desenvolvimento web 3')
print(texto)
print(texto[4])
print(texto[6:16])
print(texto[6:16:2])
print(texto[:7])
print(texto[7:])
print(texto[7: :3])
print(texto[: :4])

print(''' O python é uma linguagem fácil,é uma linguagem tipada,
trabalha em blocos.......''') #para imprimir um texto completo na tela utilizo 3 aspas simples ou duplas

# len - quantidade de caracteres que a string possui(comprimento)
print('A quantidade de caracteres na frase é: ', len(texto))

# count - conta a quantidade de vezes que a string  repete
print('A quantidade de vezes que o caractere  aparece  na frase é: ',texto.count('e'))
print('A quantidade de vezes que o caractere  aparece  na frase é: ',texto.count('e',3,13))

# find - para mostrar a posiçao que se encontra uma determinada string
print('A posição da string é: ', texto.find('web'))

# operador in - para verificar se uma determinada string existe na frase
print('Desenvolvimento' in texto)

# método replace() - para trocar uma palavra sem alterar o texto principal
print(texto.replace('web 3', 'Python'))

#exemplo alterando a frase original
texto=texto.replace('web 3', 'Python')
print(texto)

# método upper() - para colocar tudo em letra maiuscula
print(texto.upper())

# método lower() - para colocar tudo em letra minuscula
print(texto.lower())

#método capitalize - para colocar os caracteres da primeira letra  da frase em maiusculo
print(texto.capitalize())

#método title() - para transformar todas as primeiras letras de cada palavra em maiusculo
print(texto.title())

# método swapcase - inverte a caixa da string ,o que é minusculo vira maiusculo e vice versa
print(texto.swapcase())

#método strip - para remover espaços do inicio e do fim
frase=('   Aula 3 de Python   ')
print(frase)
print(frase.strip())

#método rstrip() - para remover o espaço da direita(final)
frase=('   Aula 3 de Python   ')
print(frase.rstrip())

# método lstrip() - para remover o espaço da esquerda(inicial)
frase=('   Aula 3 de Python   ')
print(frase.lstrip())

# método split() - para dividir uma string em substrings, onde cada elemento vai ser separado pelo seu splitador
print(texto.split())
print(frase.split())

# método join() - para separar os elementos da frase, usando um separador
print('-'.join(texto))
print('*'.join(frase))

#Formatação de string

# center() - para centralizar
print(texto.center(100))
print(texto.center(100,'*'))

# ljust() - alinhar a esquerda
print(texto.ljust(100))
print(texto.ljust(100,'-'))

# rjust() - alinhar a direita
print(texto.rjust(100))
print(texto.rjust(100,'@'))

# Estruturas Condicionais - simples(if), composta(else), mais de 1 condição(elif)
'''
a=7
b=6
if a>b:
    print("A variavel  a é maior.".format(a))
if a<b:
    print("A variavel  b é maior.".format(b))
#outro exemplo
nome=input('Qual o seu nome?')
if nome=='Thereza' :
    print('Esse nome é maravilhoso')
print('Boa noite, {}'.format(nome))
'''
#exemplo de condicional composta
tempo=int(input('Quantos anos tem o seu carro?'))
if tempo <=3 :
    print('Carro novo!')
else :
    print('Carro Velho')

#outro exemplo
n1=float(input('Digite a nota da AV1'))
n2=float(input('Digite a nota da AV2'))
    
m=(n1+n2)/2
print('A sua média foi {:.1f}'.format(m))
if m>=6 :
    print('Sua média foi boa. Parabéns!')
else :
    print('Sua média foi ruim.Estude mais!')

# outra forma de fazer a mesma coisa
print('Parabens!' if m>=6 else 'Estude mais!')

#exemplo de elif
x=int(input('Entre com o valor de x'))
y=int(input('Entre com o valor de y'))

if x==y :
    print('Numeros iguais')
elif y>x :
    print('Y é maior que x')
elif y<x :
    print('Y é menor que x')
else :
    print('Numeros diferentes')
