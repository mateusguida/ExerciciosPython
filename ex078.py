import os
os.system("cls") #limpa janela terminal antes da execução

maior = menor = 0

valores = []
for c in range(0,5):
    valores.append(int(input(f"Digite um valor para a posição {c}: ")))
    if c == 0:
        maior = menor = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]

print('-=' * 30)
print(f'Você digitou os valores {valores}')

print(f'O maior valor foi {maior} nas posições ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}... ', end='')
print()

print(f'O menor valor foi {menor} nas posições ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}... ', end='')
print()

