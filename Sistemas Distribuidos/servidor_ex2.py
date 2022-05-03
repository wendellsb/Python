import socket 
import threading
import validaCPF

HEADER = 64
PORT = 8000
SERVER = socket.gethostbyname('127.0.0.1')
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONECT = ""

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def atender_client(conn, addr):
    print("[NOVA CONEXAO] ",addr," Conectado ")
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONECT:
                connected = False
            num = validaCPF.validate(msg)#chamada
            print(addr," Digitou: ", msg)
            conn.send((num).encode(FORMAT))
    conn.close()  

def start():
    server.listen()
    print("[OUVINDO] O servidor esta ouvindo no endereco:", SERVER)
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=atender_client, args=(conn, addr))
        thread.start()
        print("[CONEXOES ATIVAS]" , threading.activeCount() - 1)
print("[INICIADO] O SERVIDOR ESTA INICIADO...")

start()