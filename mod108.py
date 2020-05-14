def dobro(n=0):
    return n*2

def metade(n=0):
    return n/2

def aumentar(n=0, p=0):
    return n * (1 + p/100)

def diminuir(n=0, p=0):
    return n * (1 - p/100)

def moeda(preco = 0, moeda = 'R$'):
    return f'{moeda} {preco:.2f}'.replace('.',',')