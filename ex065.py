import os
os.system("cls") #limpa janela terminal antes da execução

flag = 'S'
total = soma = 0

while flag == 'S':
    num = int(input("Digite um número: "))
    
    if total == 0:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    
    total += 1
    soma += num

    flag = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    
print(f'Você digitou {total} números e a média foi {soma/total}.')
print(f'O maior valor foi {maior} e o menor for {menor}.')