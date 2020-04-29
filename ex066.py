import os
os.system("cls") #limpa janela terminal antes da execução

total = soma = 0

while True:
    num = int(input("Digite um número [999 para parar]: "))
    if num == 999:
        break
    total += 1
    soma += num
    
print(f'Você digitou {total} números e a soma entre eles foi de {soma}.')