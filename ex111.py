from utilidades import moeda

def limpa():
    import os
    os.system("cls") #limpa janela terminal antes da execução

limpa()
preco = float(input("Digite o preço: "))
moeda.resumo(preco, 20, 12)