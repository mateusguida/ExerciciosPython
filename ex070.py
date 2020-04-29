import os
os.system("cls") #limpa janela terminal antes da execução

total = caro = 0

print("-" * 20)
print(f'LOJA SUPER BARATÃO')
print("-" * 20)

while True:
    prod = str(input("Nome do Produto: ")).strip()
    preco = int(input("Preço: R$ "))
    
    if total == 0 or preco < precoB:
        prodB = prod
        precoB = preco
    
    total += preco

    if preco > 1000:
        caro += 1
        
    op = ' '
    while op not in 'SN':
        op = str(input("Quer continuar? [S/N]")).strip().upper()[0]
    if op == 'N':
        break

print("------- FIM DO PROGRAMA -------")

print(f'O total da compra foi R$ {total:.2f}')
print(f'Temos {caro} produtos custando mais que R$ 1000.00')
print(f'O produto mais barato foi {prodB} que custa R$ {precoB:.2f}.')