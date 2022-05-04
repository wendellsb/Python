# -* - coding: utf-8 -*-

#sort () - para ordenar uma lista em ordem crescente, esse comando não altera a lista original
"""
lista=[23,12,67,45,34,54]
lista.sort()
print(lista)

#outra maneira de colocar em ordem crescente

lista=[23,12,67,45,34,54]
lista=sorted(lista)
print(lista)

#reverse() - para ordenar uma lista em ordem inversa, esse comando não altera a lista original

lista=[23,12,67,45,34,54]
lista.sort(),lista.reverse()
print(lista)

nome=['Endrigo','Flavio','Camila','Elisa']
nome.sort()
print(nome)

#Criação de lista vazia: variavel=list() ou variavel=[ ]

valores=[] #ou valores=list()
valores.append(5)
valores.append(15)
valores.append(25)
valores.append(35)
valores.append(45)
print(f'A nova lista é: {valores}')

#exemplo mostrando o indice e os valores

valores=[] #ou valores=list()
valores.append(5)
valores.append(1)
valores.append(2)

for c,v in enumerate(valores):
    print(f'Na posição {c} tenho o valor {v} !')
print('Cheguei ao final da lista!')

#exemplo usando o range e entrando com os valores

valores=list()
for cont in range(0,5):
    valores.append(int(input('Digite um valor: ')))
for i,v in enumerate(valores):
    print(f'Na posição {i} tenho o valor {v} !')
print('Cheguei ao final da lista!')

# Criar copia da lista usa-se o comando [:]

a=[2,3,4,5]
b=a[:] #copia da lista a, para que a mesma não seja alterada caso a variavel b se altere
b[2]=8

print(f'Lista A: {a}')
print(f'Lista B: {b}')

#Se não fizermos a copia da lista, quando atribuirmos um novo valor este será alterado em ambas as variaveis

a=[2,3,4,5]
b=a
b[2]=8

print(f'Lista A: {a}')
print(f'Lista B: {b}')

# Lista composta - uma lista dentro de outra lista

aluno=[['Elisa',12],['Yago',34],['Camila',5]] #criei 1 lista com 3 listas dentro
print(aluno)
print(aluno[0][0])#o primeiro valor é referente a lista e o segundo valor é referente ao indice
print(aluno[1][1])
print(aluno[1]) #quando temos um valor apenas ele pega todos os elemento da lista

#outro exemplo

pessoas=list()
pessoas.append('Matheus')
pessoas.append(19)
galera=list()
galera.append(pessoas[:])
pessoas[0]='Bianca'
pessoas[1]=18
galera.append(pessoas[:])
print(galera)"""

#Dicionário -são listas de associções composta por: chave e valores - dicionario={'chave' :  'valor'}

frutas={'A' : 'abacaxi', 'B' : 'banana'}
print(frutas)
print(frutas['A']) #busca feita pela chave
print(frutas['B'])

# criar um dicionário vazio - variavel=dict()

dados=dict()
dados={'nome' : 'Thereza', 'idade' : 20}
print(dados)
print(dados['nome'])
print(f'A {dados["nome"]} tem {dados["idade"]} anos.')

#Adicionar dados no dicionario - não pode usar o comando append no dicionário, não funciona

dados['sexo']='F'
print(dados)

dados['estado']='RJ'
print(dados)

#apagar dados do dicionário

del dados['idade']
print(dados)

"""
Keys - retornam as chaves do dicionário
values - retornam os valores
items - etornam os valores e as chaves """

filme={'titulo' : 'Star Wars', 'ano' : 1977, 'diretor' : 'George Lucas'}
print(filme.values())
print(filme.keys())
print(filme.items())

for k,v in filme.items():
    print(f'O {k} é {v}')

#exemplo de lista com dicionário dentro da lista

brasil=[]
estado1={'uf' : 'Rio de Janeiro', 'sigla': 'RJ'}
estado2={'uf' : 'São Paulo ', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[0]['uf'])
print(brasil[1]['sigla'])