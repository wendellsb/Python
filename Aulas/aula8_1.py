from tkinter import *

i=Tk()

i.title('Primeiro Aplicativo') #para inserir titulona janela

i.wm_iconbitmap('File_BMP_26637.ico') #para inserir icone na janela

i.geometry('400x300') #para definir o tamanho da janela

i['bg']='#FF00FF'  #para inserir cor de fundo na janela

i.resizable(True,True) #para bloquear o redimencionamento da janela False(0) ou True (1)

"""i.minsize(400,300) # define o tamanho minimo da janela

i.maxsize(700,400) # define o tamanho maximo da janela

i.state('zoomed') #para a ajanela abrir de forma máxima

i.state('iconic')"""

# Entry - para criar uma entrada de dados vazia para receber dados externos

ent=Entry(i)
ent.pack() #pack() - para empacotar o elemento

# Button - para inserir botão na janela

b = Button(i, text='Clique')
b.pack()

#Label - para inserir um texto(palavra) na janela

"""texto = Label(i, text='Boa noite!', bg='#FF00FF')
texto.pack()"""

texto = Label(i,
                     text='Boa noite!\n Sejam Bem Vindos!',
                     bg='red',
                     fg='yellow',
                     font='Arial 20 bold italic',
                     padx=30,
                     pady=30,
                     justify=LEFT,
                     bd=10,
                     relief='raised'
                    )
texto.pack()








i.mainloop() #para executar o Tkinter
