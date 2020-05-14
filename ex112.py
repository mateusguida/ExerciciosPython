from utilidades import moeda, dados

def limpa():
    import os
    os.system("cls") #limpa janela terminal antes da execução

limpa()
preco = dados.leiaDinheiro("Digite o preço: ")
moeda.resumo(preco, 20, 12)