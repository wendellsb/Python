from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql

#criação das funções - inserir

def insert ():
    id= e_id.get()
    nome=e_nome.get()
    email=e_email.get()

    if(id==" " or nome==" " or email==" "):
        MessageBox.showinfo('Status inserido', 'Todos os campos são obrigatórios')
    else:
        con=mysql.connect(host='localhost', user='root', password="", database='aula10')
        cursor=con.cursor()
        cursor.execute("insert into aluno values(' "+ id +" ',' "+ nome +" ',' "+ email +" ')")
        cursor.execute('commit')
        show()
        MessageBox.showinfo('Status inserido', 'Inserido com sucesso!')
        con.close()

#função para atualizar os dados

def update ():
    id= e_id.get()
    nome=e_nome.get()
    email=e_email.get()

    if(id==" " or nome==" " or email==" "):
        MessageBox.showinfo('Status atualizado', 'Todos os campos são obrigatórios')
    else:
        con=mysql.connect(host='localhost', user='root', password="", database='aula10')
        cursor=con.cursor()
        cursor.execute("update aluno set nome=' " + nome +" ',email= ' " + email +" ' where id=' " + id + " ' ")
        cursor.execute('commit')

        e_id.delete(0, 'end')
        e_nome.delete(0, 'end')
        e_email.delete(0, 'end')
        show()
        MessageBox.showinfo('Update atualizado', 'Atualizado com sucesso!')
        con.close()

#função para apagar dados

def delete ():
    if(e_id.get()==" "):
        MessageBox.showinfo('Status deletado', 'Id é compativel para deletar')
    else:
        con=mysql.connect(host='localhost', user='root', password="", database='aula10')
        cursor=con.cursor()
        cursor.execute("delete from aluno where id=' " +e_id.get() + " ' ")
        cursor.execute('commit')

        e_id.delete(0, 'end')
        e_nome.delete(0, 'end')
        e_email.delete(0, 'end')
        show()
        MessageBox.showinfo('Status deletado', 'Deletado com sucesso!')
        con.close()


#função para selecionar

def get ():
    if(e_id.get()==" "):
        MessageBox.showinfo('Status Fetch', 'Id é compativel ')
    else:
        con=mysql.connect(host='localhost', user='root', password="", database='aula10')
        cursor=con.cursor()
        cursor.execute("select * from aluno  where id=' " + e_id.get() + " ' ")
        rows= cursor.fetchall()

        for row in rows:
            e_nome.insert(0, row[1])
            e_email.insert(0, row[2])
            
        con.close()

#função para mostrar os dados dentro da listbox

def show ():
        con=mysql.connect(host='localhost', user='root', password="", database='aula10')
        cursor=con.cursor()
        cursor.execute("select * from aluno ")
        rows= cursor.fetchall()

        for row in rows:
            insertData= str(row[0] )+ '                  ' + row[1]
            list.insert(list.size() +1, insertData)
            con.close()

r=Tk()
r.geometry("600x300")
r.title('Python,Tkinter e Mysql')

id=Label(r, text='Entre com o Id', font=('Bold',10))
id.place(x=20, y=30)

nome=Label(r, text='Entre com o nome', font=('Bold',10))
nome.place(x=20, y=60)

email=Label(r, text='Entre com o email', font=('Bold',10))
email.place(x=20, y=90)

e_id=Entry()
e_id.place(x=150, y=30)

e_nome=Entry()
e_nome.place(x=150, y=60)

e_email=Entry()
e_email.place(x=150, y=90)


#inserir dados

insert=Button(r, text='Insert', font=('italic',10),bg='white', command=insert)
insert.place(x=20,y=140)

#atualizar dados

update=Button(r, text='Update', font=('italic',10),bg='white', command=update)
update.place(x=65,y=140)

#apagando dados

delete=Button(r, text='Delete', font=('italic',10),bg='white', command=delete)
delete.place(x=120,y=140)

#selecionar dados

get=Button(r, text='Select', font=('italic',10),bg='white', command=get)
get.place(x=170,y=140)

#para mostrar dentro de uma list box

list=Listbox(r)
list.place(x=290, y=30)
show()
