import os
os.system("cls") #limpa janela terminal antes da execução

from random import randint
from time import sleep

print("-=-" * 20)
print("Sou seu computador...")
print("Acabei de pensar em um número entre 0 e 10.")
print("Será que você consegue adivinhar qual foi?")
print("-=-" * 20)

num = int(input("Qual é o seu palpite? "))
count = 0
nrand = randint(0,10) #Gera numero aleatorio entre 0 e 10

while num != nrand:
    if num > nrand:
        print("Menos... Tente mais uma vez.")
    else:
        print("Mais... Tente mais uma vez.")
    count += 1
    num = int(input("Qual é o seu palpite? "))


print(f'Acertou com {count} tentativas. Parabéns')