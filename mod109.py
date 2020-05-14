def dobro(n=0, formato=False):
    return n*2 if formato is False else moeda(n*2)

def metade(n=0, formato=False):
    return n/2 if formato is False else moeda(n/2)

def aumentar(n=0, p=0, formato=False):
    res = n * (1 + p/100)
    return res if formato is False else moeda(res)

def diminuir(n=0, p=0, formato=False):
    res = n * (1 - p/100)
    return res if formato is False else moeda(res)

def moeda(preco = 0, moeda = 'R$'):
    return f'{moeda} {preco:.2f}'.replace('.',',')