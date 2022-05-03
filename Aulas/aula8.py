import mysql.connector

conexao=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='aula7'
    )

cursor=conexao.cursor()
#print(conexao)

#lastrowid - para mostrar o id da ultima linha

"""sql = "insert into pessoa (nome,idade,email) values ('Rodrigo Araujo',20,'rodrigo.araujo@soulasalle.com.br' )"
cursor.execute(sql)
conexao.commit()
print(cursor.rowcount, 'registro inserido')

print('O ultimo registro inserido, ID: ', cursor.lastrowid)"""

#select - para selecionar os registros da tabela e fetchall - método que busca todas as linhas(dados) da tabela

cursor.execute('select * from pessoa')
result=cursor.fetchall()
#print(result)

for x in result:
    print(x)


cursor.execute('select nome,idade  from pessoa')
result=cursor.fetchall()
#print(result)

for x in result:
    print(x)        

# fetchone() - retorna a primeira linha do resultado

cursor.execute('select email  from pessoa')
result=cursor.fetchone()
#print(result)

for x in result:
    print(x)   

cursor.execute('select *  from pessoa where idade>19')
result=cursor.fetchall()
#print(result)

for x in result:
    print(x)  

cursor.execute('select nome from pessoa where idade<9')
result=cursor.fetchall()
#print(result)

for x in result:
    print(x)  

# like - caracteres curingas % %, para fazer buscas especificas

cursor.execute('select idade,email from pessoa where nome like"%Rodrigo%" ')
result=cursor.fetchall()
print(result)

#order by - para classificar o resultado em ordem alfabetica crescente(asc) ou decrescente(desc)

cursor.execute('select * from pessoa order by nome')
result=cursor.fetchall()
for x in result:
    print(x)


cursor.execute('select * from pessoa order by nome desc')
result=cursor.fetchall()
for x in result:
    print(x)

cursor.execute('select * from pessoa order by idade desc')
result=cursor.fetchall()
for x in result:
    print(x)

#drop - apaga tudoooooooooo

cursor.execute('drop database aulateste')
cursor.execute('drop table aluno')

#delete - para deletar registros

cursor.execute('delete from pessoa where cod_pessoa=9')
conexao.commit()
print(cursor.rowcount,'Registro(s) deletado(s)')

#deletando vários registros

sql='delete from pessoa where cod_pessoa in (%s,%s)'
cursor.execute(sql , (11,12))
conexao.commit()
print(cursor.rowcount,'Registro(s) deletado(s)')

# between - para deletar entre intervalos

sql='delete from pessoa where cod_pessoa between %s and %s'
cursor.execute(sql , (10,14))
conexao.commit()
print(cursor.rowcount,'Registro(s) deletado(s)')

#update - parsa atualizar a tabela

cursor.execute('update pessoa set nome="Thereza Gondim" where cod_pessoa="1" ')
conexao.commit()
print(cursor.rowcount,'Registro(s) afetado(s)')

# limit - para limitar o numero de registros retornados

cursor.execute('select * from pessoa limit 2 ')
result=cursor.fetchall()
print(result)

#offset - para definir de onde começa a busca

cursor.execute('select * from pessoa limit 2 OFFSET 5')
result=cursor.fetchall()
print(result)

# max - retorna o maior valor

cursor.execute('select max(idade) from pessoa where idade >19')
result=cursor.fetchall()
print('A maior idade é: ',result)

# min - retorna o menor valor

cursor.execute('select min(idade) from pessoa where idade <50')
result=cursor.fetchall()
print('A menor idade é: ',result)

# sum - retorna a soma

cursor.execute('select sum(idade) from pessoa ')
result=cursor.fetchall()
print('A soma das idades é: ',result)

# avg - retorna a média

cursor.execute('select AVG(idade) from pessoa ')
result=cursor.fetchall()
print('A media das idades é: ',result)