import mod109

def limpa():
    import os
    os.system("cls") #limpa janela terminal antes da execução

limpa()
preco = float(input("Digite o preço: "))
print(f'A metade de {mod109.moeda(preco)} é {mod109.metade(preco, True)}')
print(f'O dobro de {mod109.moeda(preco)} é {mod109.dobro(preco, True)}')
print(f'Aumentando 10%, temos {mod109.aumentar(preco, 10, True)}')
print(f'Diminuindo 10%, temos {mod109.diminuir(preco, 10, True)}')