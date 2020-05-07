import os
os.system("cls") #limpa janela terminal antes da execução

mat = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somap = soma3c = 0

for i in range(0,3):
    for j in range(0,3):
        mat[i][j] = int(input(f"Digite um valor para [{i}][{j}]: "))
        
        # Soma dos valores pares
        if mat[i][j] % 2 == 0:
            somap += mat[i][j]
        
        # Soma dos valores da terceira coluna
        if j == 2:
            soma3c += mat[i][j]

        # Maior valor da segunda linha
        if i == 1:
            if j == 0:
                maior2l = mat[i][j]
            elif mat[i][j] > maior2l:
                maior2l = mat[i][j]

print('-=' * 20)
for i in range(0,3):
    for j in range(0,3):
        print(f'[{mat[i][j]:^5}]', end='')
    print()
print('-=' * 20)
print(f'A soma dos valores pares é {somap}.')
print(f'A soma dos valores da terceira coluna é {soma3c}.')
print(f'O maior valor da segunda linha é {maior2l}.')