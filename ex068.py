import os
os.system("cls") #limpa janela terminal antes da execução

from random import randint


print("=-" * 15)
print("VAMOS JOGAR PAR OU ÍMPAR")

vit = 0

while True:
    print("=-" * 15)
    num = int(input("Digite um valor: "))
    jogador = str(input("Par ou Ímpar? [P/I]")).strip().upper()[0]
    comp = randint(0,10)
    soma = num + comp

    print('-' * 30)
    print(f'Você jogou {num} e o computador {comp}. ', end="")

    if soma % 2 == 0:
        print(f'Total de {soma} DEU PAR')
        flag = 'P'
    else:
        print(f'Total de {soma} DEU ÍMPAR')
        flag = 'I'
    
    print('-' * 30)

    if jogador == flag:
        vit += 1
        print("Você VENCEU!")
        print("Vamos jogar novamente...")
    else:
        print("Você PERDEU!")
        break

print(f'GAME OVER! Você venceu {vit} vezes.')