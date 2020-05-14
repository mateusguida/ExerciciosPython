def leiaint(texto):
    x = input(texto)
    while x.isnumeric() == False:
        print("{}ERRO! Digite um número inteiro válido{}".format('\033[31m', '\033[m'))
        x = input(texto)
    return int(x)

def limpa():
    import os
    os.system("cls") #limpa janela terminal antes da execução

limpa()
n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')