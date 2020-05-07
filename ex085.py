import os
os.system("cls") #limpa janela terminal antes da execução

numero = [[], []]

for i in range(0,7):
    num = int(input("Digite um numero: "))

    if num % 2 == 0:
        numero[0].append(num)
    else:
        numero[1].append(num)

print('-=' * 30)
numero[0].sort()
numero[1].sort()
print(f'{numero}')