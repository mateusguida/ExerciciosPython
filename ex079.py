import os
os.system("cls") #limpa janela terminal antes da execução

maior = menor = 0

valores = []
while True:
    num = int(input(f"Digite um valor: "))
    if num in valores:
        print("Valor duplicado! Não vou adicionar...")
    else:
        valores.append(num)

    flag = str(input("Quer continuar? [S/N]")).lower()
    if flag == 'n':
        break

print('-=' * 30)
valores.sort()
print(f'Você digitou os valores {valores}')