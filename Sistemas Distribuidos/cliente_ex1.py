import socket

host= '127.0.0.1'
porta = 50000

s = socket.socket()
s.connect((host, porta))

mensagem = input('Digite a frase: ')
mensagemAux = mensagem

s.sendall(str.encode(mensagem))
data = s.recv(4096)
print('Mensagem criptografada: ', str(data.decode()))
mensagem = str(data.decode())
s.close()

s = socket.socket()
s.connect((host, porta))
s.sendall(str.encode(mensagem))
data = s.recv(4096)
print('Mensagem ecoada', str(data.decode()))
mensagem = (data.decode())

if(mensagem == mensagemAux):
    print('A criptografia funciona!')