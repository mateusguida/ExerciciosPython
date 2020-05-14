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

def resumo(n=0, acr=10, dec=5):
    print('-' * 30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-' * 30)
    print(f'{"Preço analisado:":<20}', end='')
    print(f'{moeda(n):<10}')
    print(f'{"Dobro do preço:":<20}', end='')
    print(f'{dobro(n, True):<10}')
    print(f'{"Metade do preço:":<20}', end='')
    print(f'{metade(n, True):<10}')
    print(f'{acr}% {"de aumento:":<16}', end='')
    print(f'{aumentar(n, acr, True):<10}')
    print(f'{dec}% {"de aumento:":<16}', end='')
    print(f'{diminuir(n, dec, True):<10}')
    print('-' * 30)