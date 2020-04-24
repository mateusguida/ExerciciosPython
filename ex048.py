import os
os.system("cls") #limpa janela terminal antes da execução

soma = 0
qtd = 0

for c in range(3,500,3):
    soma += c
    qtd = qtd + 1

print(f"A soma de todos os {qtd} valores solicitados é {soma}")