import os
os.system("cls") #limpa janela terminal antes da execução

valores = []
while True:
    valores.append(int(input(f"Digite um valor: ")))
    flag = str(input("Quer continuar? [S/N]")).lower()
    if flag == 'n':
        break
        
print('-=' * 30)
valores.sort(reverse=True)
print(f'Você digitou {len(valores)} valores.')
print(f'Lista em ordem decrescente: {valores}')
if 5 in valores:
    print("O número 5 está na lista")
else:
    print("O número 5 não está na lista")