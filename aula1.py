# -*-  coding: utf-8  -*-

#comando para saida de dados - print

print('Boa noite')

print(10)

print('20')

print('Eu tenho, 2 ,cachorras lindas')

print('Eu tenho' , 2, 'cachorras lindas!')

print('Sejam  \n Bem Vindos')

#No python toda variavel é um objeto; as variavesi devem ser declaradas com letras minusculas;

#as variaveis podem ser do tipo : string, float, int, booleano

num = 2   #criação de variavel
print('Eu tenho', num, 'cachorras lindas!')


x=12
y=123
z=45

print('O valor de x é: ', x)

x=y=z
print('O valor de x é: ', x)

x=y=z=12

print(x)
print(y)
print(z)

#podemos declarar varias variaveis de uma unica vez

x,y,z=12,123,45

print(x)
print(y)
print(z)

# Operadores logicos: soma (+,)  subtração ( - ),  multiplicação( *), divisão (/),  divisão do inteiro (//) ,  exponenciação (**),  modulo (%)

#exemplo da soma

a=10
b=3
c=2

#a,b,c=10,8,2 outra maneira de declarar as variaveis

soma=a+b
print('A soma de a + b é: ', soma)

#exemplo da divisão

media=(a + b) / 2
print('A divisão de a + b é: ', media)

media=(a + b) / c
print('A divisão de a + b é: ', media)

#exemplo de potencia

elevado= c**2
print('A potência de c  é: ', elevado)

#exemplo de valor inteiro da divisão

div_int= a // b
print('O valor inteiro da divisão é: ', div_int)


#exemplo de resto da divisão (modulo)

div_int= a % b
print('O resto da divisão é: ', div_int)

# os sinais possuem preferência, logo: * , /, //, %,** tem preferência ao sinal de + e  -

resposta= 10 + 5 * 3 / 15
print(' A resposta é: ', resposta)

d= (10 + 5 ) * 3 / 15
print(' A resposta é: ', d)
