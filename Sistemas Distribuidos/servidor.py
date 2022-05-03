import socket 
from threading import *

def cripto(msg):
        global chamadas, mutex 
        
        print('Conectado')
        data = msg.recv(4096)
   
        dataAux = str(data.decode())
        print('Passei do while')
        zenit, polar = 'zenit', 'polar'
        final_message = ''
        n = 0
        for i in range(len(dataAux)):
                x = dataAux[n]
                if x in zenit:
                        x = int(zenit.find(dataAux[n]))
                        final_message += polar[x]
                elif x in polar:
                        x = int(polar.find(dataAux[n]))
                        final_message += zenit[x]
                else:
                        final_message += dataAux[n]
                n += 1
                            
        data = bytes(final_message, 'utf-8') 
        msg.sendall(data)
        with mutex:
                chamadas+=1
        print(chamadas)
        msg.close()
          
host = 'localhost'
porta = 50000

s = socket.socket()
s.bind((host, porta))
s.listen()
print('Aguardando conexão de um cliente')

chamadas = 0
mutex = Lock()

while True:
        conn, ender = s.accept()
        print ("Recebi uma conexão")
        Thread(target=cripto, args=(conn,)).start()