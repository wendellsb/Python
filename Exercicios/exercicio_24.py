cidade = input('Informe sua cidade: ')
cidade = cidade.upper()
r = cidade.find('SANTO')
res = 'SANTO' in cidade

print(r)
print(res)