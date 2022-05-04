#  -*- coding: utf-8 -*-

#estrutura de repetição for - para percorrer os itens de uma lista, ou tupla ...intervalo, para usarmos
# o for precisamos saber  o limite inicial e final
nome= ['Camila', 'Flavio', 'Luana']
for n in nome :
    print('Os nomes da lista são: ', n)


for c in range(0,10):
    print(c)

for i in range(0,6) :
    print('Olá')

for i in range(10) :
    if  i%2==0 :
        print(i, 'É numero par')
    else :
         print(i, 'É numero ímpar')

# Estrutura de repetição While - vai ser executado enquanto for verdadeiro

contador= 0
while contador < 5 :
    print(contador)
    contador = contador + 1

#exemplo usando flag

senha= ' '
while senha != 'segredo' :
    senha=input('Por favor digite a sua senha de acesso')
    if senha =='segredo' :
        print('Acesso liberado!')
    else:
        print('Acesso negado!')

#exemplo de numeros pares e impares

n=1
par=0
impar=0
while n!=0:
    n=int(input('Digite um valor'))
    if n % 2==0:
         par +=1
    else:
        impar +=1
#print('Você digitou {} numeros pares e {} numeros impares!'.format(par,impar))
print(f'Você digitou {par} numeros pares e {impar} numeros impares!')

#exemplo de print usando f de string

nome= 'Thereza'
idade=20

print('A {} tem {} anos'.format(nome,idade))
print(f'A {nome} tem {idade} anos') #usando f de string

#Variaveis compostas possuem 3 tipos: Tuplas ( ), lista [ ], Dicionário { }
# As tuplas são imutáveis (não podem ser alteradas)

aluno =('Luana','Endrigo','Flavio','Wendell')
#aluno ='Luana','Endrigo','Flavio','Wendell' no python novo não precisa usar o parenteses para definir a tupla
print(aluno)

print(aluno[1])
print(aluno[-2]) #mostra de tras para frente
print(aluno[1:3])
print(aluno[1:])
print(aluno[:3])

for a in aluno:
    print(f'Os alunos são: {aluno}')
print('Essa turma é nota 1000')

#outro exemplo, usando o range

lanche=('Hamburguer','Suco', 'Pizza','Bolo')
for cont in range(0, len(lanche)) : #len - para mostrar a quantidade de elementos de uma string
    print(f'Eu vou comer {lanche[cont]}')
print('Depois de comer tudo isso vou rolar igual uma bola!!!')

#outra forma de fazer usando o enumarate, para mostrar a posição dos elementos

for pos, comida in enumerate(lanche) :
    print(f'Eu vou comer: {comida} na posição {pos}')
print('Comi muito!')

#quando usamos tupla o sinal de + concatena

a=(2,4,6)
b=(5,8,2,1)
c=a+b
print(c)

#len() - quantidade de elementos de uma string

nome = ('Debora', 'Luana','Daniel','Maria')
tam=len(nome)
print('O tamanho da lista é: ',tam)

teste='Oi!'
print(teste)
print(len(teste))
print(teste[0])
print(teste[1])
print(teste[2])

#count() -  conta quantas vezes um determinado elemento se repete

a=(2,5,6)
b=(5,8,2,1)
c=a+b
print('O numero 5 se repete:' , c.count(5))

#index() - para saber a posição que o elemento se encontra, quando o elemento for 
# repetido ele mostra a primeira posição

print('O 5 encontra-se na posição: ',c.index(5))

#del() - para deletar elementos

lista=(1,2,3,4,5)
#print(lista)
del(lista) 

#listas - são semelhantes as tuplas, são representadas por [ ]; as listas são mutáveis(podem ser alteradas)

nome = ['Debora', 'Luana','Daniel','Maria']
print(nome)
print('O nome que encontra-se na posição 3 é: ', nome[3])

num=[2,5,9,1]
print(num)
num[2]=3 #alterando o valor da posição 2 de 9 para 3
print(num)

#min() - para mostrar o menor valor
numeros=[10.55, 67, 90.2, 10, 21.7]
print('O menor valor da lista é: ', min(numeros))

#max() - para mostrar o maior valor
print('O maior valor da lista é: ', max(numeros))

#sum() - para somar todos os valores da lista
num1 = [10,20,30,40,50]
print('A soma dos valores da lista é: ',sum(num1))

#append() - para adicionar elementos no final da lista
lista = [1,2,3,4,5]
lista.append('maça')
print(lista)

#insert() - para adicionar elementos na posição que vc quiser
lanche=['Hamburguer','Suco', 'Pizza','Bolo']
lanche.insert(2,'maça')
print(lanche)

#pop() - apaga o ultimo elemento da lista
lanche.pop()
print('A nova lista é: ',lanche)

lanche.pop(2) #definindo a posição a ser apagada
print('A nova lista é: ',lanche)
#del() - para remover um determinado elemento da lista

del lanche[2]
print(lanche) 

lanche=['Hamburguer','Suco', 'Pizza','Bolo']
del lanche[2:]
print(lanche)

del lanche[ : ]
print(lanche)

#remove() - apaga pelo elemento e não pela posição
lanche=['Hamburguer','Suco', 'Pizza','Bolo']
lanche.remove('Pizza')
print(lanche)

#criando uma lista usando o range
valor = list(range(4,11))
print(valor)

# valores.sort() coloca em ordem
# valores.sort(reverse=True) coloca em ordem inversa

# para criar uma nova lista da forma correta
a = [2, 3, 4, 7]
b = a[:]
b[2] = 8