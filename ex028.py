from random import randint
from time import sleep

print("-=-" * 20)
print("Vou pensar em um número entre 0 e 5. Tente adivinhar!")
print("-=-" * 20)

nrand = randint(0,5) #Gera numero aleatorio entre 0 e 5

num = int(input("Em que número eu pensei? "))
print("PROCESSANDO...")
sleep(1) #faz o computador esperar 3 segs para dar a impressão de processamento

if nrand == num:
    print("PARABÉNS! Você conseguiu me vencer!")
else:
    print(f'GANHEI! Eu pensei no número {nrand} e não no {num}!')