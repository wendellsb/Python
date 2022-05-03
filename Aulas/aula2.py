# -*- coding: utf-8 -*-

#operadores relacionais: igual ==; diferente !=; maior >; menor <; maior igual >=; menor igual <=

x= 2
y= 3
print(x==y)

print(x<y)
print(x>y)
print(x<=y)

soma = x +y
print(soma == x)

#operadores lógicos: and, or ,not

soma = x +y
print(x==y and x==soma)

a=3
b=3
c=4

print(a==b or a==c and c==b)

#input - comando para receber dados

x1=input('Digite o primeiro valor ')
y1=input('Digite o segundo valor ')
print(x1==y1)

n1=int(input('Digite o primeiro valor '))
n2=int(input('Digite o primeiro valor '))

print(n1, '+' , n2 , '=', n1 + n2)
print('A soma de', n1, '+' , n2 , '=', n1 + n2)
print(type(n1))

num1=float(input('Digite o primeiro valor '))
num2=float(input('Digite o primeiro valor '))

print(num1,'-', num2, '=',num1 - num2)

#forma atual de utilização do print, usando .format
 
print('A soma de {} + {} = {} ' .format(n1, n2, n1+ n2))
print('A subtração de {} - {} = {} ' .format(n1, n2, n1- n2))
print('A multiplicação de {} * {} = {} ' .format(n1, n2, n1* n2))
print('A divisão de {} / {} = {} ' .format(n1, n2, n1/ n2))
print('A divisão do inteiro de {} // {} = {} ' .format(n1, n2, n1// n2))
print('O resto da divisão  {} % {} = {} ' .format(n1, n2, n1% n2))

a=input('Entre com o seu nome ')
print(type(a))

"""para trabalharmos com  módulos usamos o comando import, esse comando vai trazer tudo que estiver dentro do modulo,
seu eu quiser trazer algo especifico do modulo uso a condição from.
exemplo - import bebida (vai trazer todo o conteudo que tiver no modulo bebida)
          from doce import pudim(vai trazer apenas o conteudo pudim que esta dentro do modulo doce)
math - significa matematica, vai trazer algumas funcionalidades matemáticas extras. Quando usarmos o import math teremos
um monte de funcionalidades extras.
exemplo: para arredondar o valor para cima uso o comando ceil
         para arredondar o valor para baixo uso o comando floor
         para eliminar o valor da frente da virgula sem arredondar nada uso o comando  trunc
         raiz quadrada uso o comando sqrt
         para calcular o fatorial uso o comando factorial
OBS: se usarmos o comando import math ela traará todas as funcionalidades de uma única vez
     import math import sqrt - vai trazer apenas a funcionalidade da raiz quadrada.
     import math import sqrt,ceil - vai trazer a funcionalidade daraiz e o arredondamento para cima"""

import math #importa todas as funcionalidades
num = int(input('Digite um numero '))
raiz = math.sqrt(num)
print('A raiz quadrada de {} é igual a {}'. format(num,math.ceil(raiz) ) )

#round - para arredondar matemáticamente
#ceil - arrendonda o valor obrigatoriamente para cima
#floor - arrendonda o valor obrigatoriamente para baixo

from math import sqrt,floor  #importa somente 2 funcionalidades

num = int(input('Digite um numero '))
raiz = sqrt(num)
print('A raiz quadrada de {} é igual a {}'. format(num,math.floor(raiz) ) )

# random - para gerar numeros aleatórios

import random  #criar numeros aleatórios entre 0 e 1
r =random.random()
print(r)

import random #criar numeros aleatorios definindo o intervalo
r1 = random.randint(5,20)
print(r1)

# ou

import random #criar numeros aleatorios definindo o intervalo
r2 = random.randrange(1,10)
print(r2)