import os
os.system("cls") #limpa janela terminal antes da execução

mat = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(0,3):
    for j in range(0,3):
        mat[i][j] = int(input(f"Digite um valor para [{i}][{j}]: "))

print('-=' * 20)

for i in range(0,3):
    for j in range(0,3):
        print(f'[{mat[i][j]:^5}]', end='')
    print()