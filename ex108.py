import mod108

def limpa():
    import os
    os.system("cls") #limpa janela terminal antes da execução

limpa()
preco = float(input("Digite o preço: "))
print(mod108.moeda(preco))
print(f'A metade de R$ {preco:.2f} é R$ {mod108.metade(preco):.2f}')
print(f'O dobro de R$ {preco:.2f} é R$ {mod108.dobro(preco):.2f}')
print(f'Aumentando 10%, temos {mod108.aumentar(preco, 10):.2f}')
print(f'Diminuindo 10%, temos {mod108.diminuir(preco, 10):.2f}')