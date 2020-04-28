import os
os.system("cls") #limpa janela terminal antes da execução

print("Digite um número para")
num = int(input("calcular seu Fatorial: "))

print(f'Calculando {num}! = ',end='')

fat = 1
while num != 1:
    print(f'{num}', end=' x ')
    fat = fat * num
    num -= 1

print(f'1 = {fat}')