def soma(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2
    
def div(n1,n2):
    return n1/n2
    
def mult(n1,n2):
    return n1*n2

def fatorial(n):
    f=1
    for c in range(1,n+1):
        f*=c
    return f

def dobro(n):
    return n*2

def triplo(n):
    return n*3

def mensagem():
    print("Boa noite!\n")

def fibo(n):
    resultado=[0]
    a,b=0,1
    while b<n:
        resultado.append(b)
        a,b=b, a+b
    return resultado