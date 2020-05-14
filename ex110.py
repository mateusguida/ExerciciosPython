import mod110

def limpa():
    import os
    os.system("cls") #limpa janela terminal antes da execução

limpa()
preco = float(input("Digite o preço: "))
mod110.resumo(preco, 20, 12)