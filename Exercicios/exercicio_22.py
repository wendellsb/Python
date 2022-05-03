nome = str(input('Informe o seu nome completo: '))

maiuscula = nome.upper()
minuscula = nome.lower()
numeros_letras = nome.replace(' ', '')
numeros_letras = len(numeros_letras)
primeiro_nome = nome.split()
primeiro_nome = primeiro_nome[0]

print(nome)
print(maiuscula)
print(minuscula)
print(numeros_letras)
print(primeiro_nome)