def sorteia(num):
    from random import randint
    from time import sleep
    lista = []
    print(f'Sorteando {num} valores da lista: ', end='')
    for i in range(0,num):
        lista.append(randint(0,10))
        print(f'{lista[i]} ', end='')
    print('PRONTO!')
    return lista

def somaPar(lista):
    tam = len(lista)
    soma = 0
    for i in range(0,tam):
        if lista[i] % 2 == 0:
            soma += lista[i]
    print(f'Somando os valores pares de {lista}, temos {soma}')

def limpa():
    import os
    os.system("cls") #limpa janela terminal antes da execução

limpa()
l = sorteia(5)
somaPar(l)
print()
