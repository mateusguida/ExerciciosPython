import os
os.system("cls") #limpa janela terminal antes da execução

num = int(input("Digite um número [999 para parar]: "))
total = soma = 0

while num != 999:
    total += 1
    soma += num
    num = int(input("Digite um número [999 para parar]: "))
    
print(f'Você digitou {total} números e a soma entre eles foi de {soma}.')