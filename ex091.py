import os
os.system("cls") #limpa janela terminal antes da execução

from time import sleep
from random import randint
from operator import itemgetter

rank = list()
jogo = dict()
print("Valores sorteados")

for c in range(1,5):
    k = 'jogador' + str(c)
    jogo[k] = randint(1,6)
    print(f'{k} tirou {jogo[k]} no dado.')
    sleep(0.5)

print('-=' * 20)
rank = sorted(jogo.items(), key=itemgetter(1), reverse=True)

print(f'  == RANKING DOS JOGADORES ==')
for i, v in enumerate(rank):
    print(f'   {i+1}° lugar: {v[0]} com {v[1]}.')
    sleep(0.5)
print()

