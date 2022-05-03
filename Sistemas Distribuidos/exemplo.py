import threading
import time

global var

var = False

def funcao(msg):
    for i in range(5):
        if var:
            break
        
        print(i, msg)
        time.sleep(1)

print('Iniciou')
threading.Thread(target=funcao, args=('vez de execução', )).start()
time.sleep(5)
print('terminou')
var = True