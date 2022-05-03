import mysql.connector

conexao=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="aula7"
    )

cursor=conexao.cursor()
#print(conexao)

#para criar a base de dados

"""cursor.execute('create database aula7')"""

#para visualizar todas as bases de dados existentes

"""cursor.execute("show databases")
for x in cursor:
    print(x)"""

#para criar tabela - create table

"""cursor.execute('create table pessoa(cod_pessoa int primary key auto_increment,nome varchar(40) not null,idade int(3),email varchar(255))')"""

#para mostrar as tabelas do banco de dados -show tables

"""cursor.execute("show tables")
for a in cursor:
    print(a)"""

#para descrever a tabela - desc ou describe

"""cursor.execute("desc pessoa")
for a in cursor:
    print(a)"""

# para inserir dados na tabela - insert into nome da tabela (atributos) values (valores)

"""sql="insert into pessoa(nome,idade,email) values ('Thereza Gondim',49,'prof.thereza.gondim@soulasalle.com.br')"
cursor.execute(sql)
conexao.commit()
print(cursor.rowcount, "registro(s) cadastrado(s)")"""

# outra maneira de fazer a mesma  coisa

"""cursor.execute("insert into pessoa(nome,idade,email) values ('Camila',19,'camila@soulasalle.com.br')")
conexao.commit()
print(cursor.rowcount, "registro(s) cadastrado(s)")"""

#para inserir vários dados simultâneamente

sql="insert into pessoa(nome,idade,email) values (%s,%s,%s)"
val=[('Camila Figueiredo',28,'camila@soulasalle.com.br'),
        ( 'luana',21,'luana@soulasalle.com.br'),
        ('Daigaro',22,'daigaro@soulasalle.com.br'),
         ('Daniel',19,'daniel@soulasalle.com.br'),
     ]
cursor.executemany(sql,val)
conexao.commit() #para salvar as alterações
print(cursor.rowcount, "registro(s) cadastrado(s)")
