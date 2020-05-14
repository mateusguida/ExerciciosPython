def fatorial(num, show=False):
    """
    -> Calcula o fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta
    :return: O valor do fatorial de um número n
    """    
    f = 1
    for c in range(num, 0, -1):
        f *= c
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
    print(f)

def limpa():
    import os
    os.system("cls") #limpa janela terminal antes da execução

limpa()
fatorial(5, True)
fatorial(3, False)
fatorial(2)
help(fatorial)
