import os
os.system("cls") #limpa janela terminal antes da execução

num = int(input("Digite um número para ver a sua tabuada: "))

print("-" * 12)
for c in range(1,11):
    print(f'{num} x {c:2} = {num*c}')
print("-" * 12)