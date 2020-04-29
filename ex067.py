import os
os.system("cls") #limpa janela terminal antes da execução

while True:
    num = int(input("Digite um número para ver a sua tabuada: "))

    if num < 0:
        break

    print("-" * 12)
    for c in range(1,11):
        print(f'{num} x {c:2} = {num*c}')
    print("-" * 12)

print("PROGRAMA TABUADA ENCERRADO! Volte sempre!")