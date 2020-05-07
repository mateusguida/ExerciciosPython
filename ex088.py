import os
os.system("cls") #limpa janela terminal antes da execução
from time import sleep
from random import randint

aposta = list()
palp = list()


print('-' * 30)
print(f"{'JOGA NA MEGA SENA':^30}")
print('-' * 30)

qtd = int(input("Quantos jogos você quer que eu sorteie? "))
print()
print('-=' * 3, f' SORTEANDO {qtd} JOGOS > ', '-=' * 3)

for c in range(1,qtd+1):
    print(f'Jogo {c}: ', end='')
   
    cont = 0
    while True:
        num = randint(1,60)
        if num not in palp:
            palp.append(num)
            cont += 1
        if cont >= 6:
            break
    palp.sort()
    print(palp)
    aposta.append(palp[:])
    palp.clear()
    sleep(0.5)

print('-=' * 5, ' < BOA SORTE! > ', '-=' * 5)
print()

