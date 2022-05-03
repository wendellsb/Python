from tkinter import *

i=Tk()

i.title('Ultima Aula')
i.geometry('400x300')
i.wm_iconbitmap('File_BMP_26637.ico')

#alinhando um elemento na janela

"""l=Label(i,
        text='Testando \n outro texto \n novo texto',
        font='Verdana 20',
        bd=1,
        relief='solid',
        padx=30,
        pady=10,
        justify=CENTER
        )

l.pack()"""

#sistema grid
"""
label1=Label(i,text='Testando', font='Arial 20', bg='red')
label2=Label(i,text='Testando1', font='Arial 20', bg='yellow')
label3=Label(i,text='Testando2', font='Arial 20', bg='blue')"""

"""label1.grid(row=0, column=0)
label2.grid(row=0, column=1)
label3.grid(row=0, column=2)"""

#exemplo de diagonal

"""label1.grid(row=0, column=0)
label2.grid(row=1, column=1)
label3.grid(row=2, column=2)"""

#exemplo com botão

"""btn1=Button(i,text='Click1')
btn2=Button(i,text='Click2')
btn3=Button(i,text='Click3')

btn1.grid(row=1,column=0)
btn2.grid(row=1,column=1)
btn3.grid(row=1,column=2)"""

#agrupando colunas e definindo coordenadas

"""label1=Label(i, width=10, text='Testando', font='Bodoni 20', bg='red').grid(column=0)
label2=Label(i, width=10, text='Testando1', font='Bodoni 20', bg='yellow').grid(column=1)
label3=Label(i, width=10, text='Testando2', font='Bodoni 20', bg='blue').grid(column=2)
label4=Label(i, width=20, text='Testando3', font='Bodoni 20', bg='yellow').grid(columnspan=2, stick=W)
#label4=Label(i, width=20, text='Testando3', font='Bodoni 20', bg='yellow').grid(columnspan=3, stick=E)

stick - permite definir as coordenas W(joga tudo para esquerda) e E(joga tudo para direita)
columnspan - para agrupar colunas
"""


"""#inserir imagem - editor online(pixlr.com/x)

img=PhotoImage(file='mickeynova.png')
label_imagem=Label(i,image=img).pack()

#label_imagem.pack()"""

#checkbox - para seleção multipla

"""texto=Label(i,
                   text='Escolha o esporte de sua preferência',
                    bg='yellow',
                    fg='blue'
            )
texto.pack()

ckeck=Checkbutton(i,text='Basquete').pack()
ckeck=Checkbutton(i,text='Natação').pack()
ckeck=Checkbutton(i,text='Futebol').pack()
ckeck=Checkbutton(i,text='Surf').pack()"""

"""#listbox - para criar uma lista

lista=Listbox(i,selectmode=EXTENDED) # extended - para poder selecionar vários itens na lista
                  
lista.pack()

#inserindo 1 item de cada vez, usamos o insert e passamos 2 parametros(index,elemento)

lista.insert(0,'Primeiro item')
lista.insert(1,'Segundo item')
lista.insert(2,'Terceiro item')

#inserindo de forma sequencial - END

lista.insert(END,'Quarto item')
lista.insert(END,'Quinto item')
lista.insert(END,'Sexto item')

#inserindo vários itens simultaneamente

nomes=['Thereza','Endrigo','Nathan','Yago','Luana','Daniel']
for nome in nomes:
       lista.insert(END,nome)
"""
"""
#inserindo escala - Scale (define o tamanho minimo e maximo) from_=Valor(define o tamanho minimo) e to=valor(define o tamanho maximo)

slide=Scale(i, from_=0, to=100).pack()
#slide.pack()

slide=Scale(i, from_=0, to=100, orient=HORIZONTAL)
slide.pack()

slide=Scale(i, from_=0, to=100, orient=HORIZONTAL, resolution=0.5)
slide.pack()

#seleção simples - Radiobutton

valor_a=IntVar()

ra_1=Radiobutton(i, text='Opção 1', variable=valor_a, value=1)
ra_2=Radiobutton(i, text='Opção 2', variable=valor_a, value=2)
ra_3=Radiobutton(i, text='Opção 3', variable=valor_a, value=3)

ra_1.pack()
ra_2.pack()
ra_3.pack()

ra_1.select() #para já deixar habilitado"""

#criando menu

"""meuMenu=Menu(i)

meuMenu.add_command(label='Arquivo')
meuMenu.add_command(label='Editar')
meuMenu.add_command(label='Formatação')

i.config(menu=meuMenu)"""

"""#criando submenus

meuMenu=Menu(i)

arquivoMenu=Menu(meuMenu,tearoff=0)

arquivoMenu.add_command(label='Novo')
arquivoMenu.add_command(label='Abrir')
arquivoMenu.add_command(label='Salvar')
meuMenu.add_cascade(label='Arquivo', menu=arquivoMenu)

i.config(menu=meuMenu)

#submenu editar


editarMenu=Menu(meuMenu,tearoff=0)

editarMenu.add_command(label='Copiar')
editarMenu.add_command(label='Colar')
editarMenu.add_command(label='Selecionar')
meuMenu.add_cascade(label='Editar', menu=editarMenu)

i.config(menu=meuMenu)"""

#exemplo de login

l_usuario=Label(i,text='Usuario:').grid(row=0, stick=W)
l_senha=Label(i,text='Senha:').grid(row=1, stick=W)

e_usuario=Entry(i).grid(row=0, column=1)
e_senha=Entry(i).grid(row=1, column=1)

btn=Button(i, text='Login').grid(row=2,column=1, stick=E)