import os
os.system("cls") #limpa janela terminal antes da execução

from random import randint
from time import sleep

print("Suas opções:")
print("[ 0 ] PEDRA")
print("[ 1 ] PAPEL")
print("[ 2 ] TESOURA")
op = int(input("QUal é a sua jogada? "))
cp = randint(0,2)
win = True

if op == 0:
    op = 'PEDRA'
    if cp == 0:
        win = 1
    elif cp == 1:
        win = 2
    else:
        win = 0

elif op == 1:
    op = 'PAPEL'
    if cp == 0:
        win = 0
    elif cp == 1:
        win = 1
    else:
        win = 2

elif op == 2:
    op = 'TESOURA'
    if cp == 0:
        win = 2
    elif cp == 1:
        win = 0
    else:
        win = 1

else:
    print('Opção Inválida!')

if cp == 0:
    cp = 'PEDRA'
elif cp == 1:
    cp = 'PAPEL'
else:
    cp = 'TESOURA'

print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!!")

print('-=-' * 10)
print('Computador jogou {}{}{}'.format('\033[31m', cp, '\033[m'))
print('Jogador jogou {}{}{}'.format('\033[35m', op, '\033[m'))
print('-=-' * 10)

if win == 0:
    print("JOGADOR VENCE")
elif win == 1:
    print("EMPATOU")
else:
    print("COMPUTADOR VENCE")

