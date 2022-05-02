#-*- coding: utf-8 -*-
#Função (def) -  esta ligada a uma palavra chamada rotina
#exemplo: criar uma função para mostrar linha
'''
def mostraLinha():
    print('-' * 30)

mostraLinha()
print('Desenvolvimento Web 3')
mostraLinha()
print('Atv Int 3')
mostraLinha()
print('Banco de dados')

#exemplo passando parametro na função

def teste(txt):
    print('-' * 30)
    print(txt)
    print('-' * 30)

teste('Bom Dia!')
teste('Boa Tarde!')
teste('Boa Noite')

#outro exemplo
a=4
b=6
s=a+b
print(s)

a=14
b=16
s=a+b
print(s)

def soma(a,b):
    s=a+b
    print(s)

mostraLinha()
soma(2,4)
soma(7,8)
soma(2,1)
mostraLinha()

#empacotar parametros
def contador(* num):
    tam=len(num)
    print('Recebi os valores {} e são ao todo {}'.format(num,tam))

contador(5,7,1,2,3)
contador(9,4,7)
contador(4,10)

def dobra(lista):
    pos=0
    while pos<len(lista):
        lista[pos] *= 2
        pos += 1

valores=[5,2,3,4,1]
print(valores)
dobra(valores)
print(valores)

#interactive help - é usada para obter informações sobra a documentação do modulo, classe, função

#help(print)
#help(input)

#docstring- usando como comentario para documentar, explicar o codigo
"""escreve o comentario"""

def cont(i,f,p):
    """ i - valor inicial
        f - valor final
        p - passo para a contagem""" 

    c=i
    while c <= f:
        print(f'{c}', end='..') 
        c +=p
    print('Fim')

help(cont)
cont(2,10,2)

#parametros opcionais -  pode-se passar ou não os valores
#def somar(a=0, b=0, c=0):

def somar(a,b,c=0):
    s=a+b+c
    print('A soma {} + {} + {} = {}'.format(a,b,c,s))
    print(f'A soma vale {s}')

mostraLinha()
somar(5,6,7)
somar(3,4)

#escopo das variaveis - variaveis globais são definidas no programa principal e as variaveis locais são definidas dentro da função
def teste1():
    n1=4
    print('N1 local vale {}'.format(n1))

mostraLinha()
n1=2
teste1()
print('N1 global vale {}'.format(n1))
mostraLinha()

#outro exemplo

def teste2(b):
    b=a+4
    c=2
    print('A local vale {}'.format(a))
    print('A global vale {}'.format(a))
    print('B local vale {}'.format(b))
    print('B global vale {}'.format(b))
    print('C local vale {}'.format(c))
    print('C global vale {}'.format(c))

mostraLinha()
a=5
teste2(a)
print('A fora vale {}'.format(a))

#retorno de resultados - return
def somar(a=0,b=0,c=0):
    s=a+b+c
    return s

mostraLinha()
print(somar(5,6,7))
print(somar(3,4))
print(somar(3))

#exemplo criando variavel
mostraLinha()
a1=somar(3,3,4)
a2=somar(4,7)
a3=somar(1)

print('A soma de {}, {}, {}'.format(a1,a2,a3))
print(f'a soma {a1}, {a2}, {a3}')

#exemplo para mostrar se o numero é par ou impar
def par(n=0):
    if n%2==0:
        return True
    else:
        return False
mostraLinha()
num=int(input('Digite um numero inteiro:  '))
print(par(num))

#mesmo exemplo usando o if dentro do programa principal
mostraLinha()
num=int(input('Digite um numero inteiro:  '))
if par(num):
    print('Numero par!')
else:
    print('Numero impar!')
'''
'''
###########################################
###########################################
###########################################
#Módulos - a ideia basica é a reutilização do codigo usando o import
import uteis #uteis o nome do arquivo criado
n1=int(input('Digite um numero inteiro: '))
n2=int(input('Digite um numero inteiro: '))

c=uteis.soma(n1,n2)
print('A soma é: ', c)

c1=uteis.mult(n1,n2)
print('A multiplicação é: ', c1)

fat=uteis.fatorial(n1)
print('o fatorial de {} é {}'.format(n1, fat))

#formar de importar
print('O dobro de {} é {}'.format(n1,uteis.dobro(n1)))
print('O triplo de {} é {}'.format(n1,uteis.triplo(n1)))

import uteis
uteis.mensagem()

print('A sequencia de fibonacci')
fib=uteis.fibo(n1)
print('O fibonacci é: ', fib)

#exemplo com módulos internos (random) e o nosso proprio
import uteis
import random

uteis.mensagem()
n=random.randint(1,10)

print('Calculando o fatorial do numero gerado')
fat=uteis.fatorial(n)
print('O fatorial de ',n,'é', fat)

print('Exibindo a sequencia de Fibonacci')
fib=uteis.fibo(n)
print('O fibonacci é: ',fib)
'''
#outra maneira de trabalhar com modulos - from

#tras o que eu peço -- from uteis import fatorial, dobro
from uteis import * #tras tudo

num=int(input('Digite um valor inteiro: '))
fat=fatorial(num)
print('O fatorial de {} é {}'.format(num,fat))
print('O dobro de {} é {}'.format(num,dobro(num)))
print('O triplo de {} é {}'.format(num,triplo(num)))