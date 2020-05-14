import mod107

def limpa():
    import os
    os.system("cls") #limpa janela terminal antes da execução

limpa()
preco = float(input("Digite o preço: "))
print(f'A metade de R$ {preco:.2f} é R$ {mod107.metade(preco):.2f}')
print(f'O dobro de R$ {preco:.2f} é R$ {mod107.dobro(preco):.2f}')
print(f'Aumentando 10%, temos {mod107.aumentar(preco, 10):.2f}')
print(f'Diminuindo 10%, temos {mod107.diminuir(preco, 10):.2f}')