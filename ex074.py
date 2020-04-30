import os
os.system("cls") #limpa janela terminal antes da execução

from random import randint

sorteio = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10),)

print(f'Os números sorteados foram: {sorteio}')
sorteio = sorted(sorteio)
print(f'O menor número foi: {sorteio[0]}')
print(f'O maior número foi: {sorteio[4]}')

# Outra opção

# print(f'O menor número foi: {min(sorteio)}')
# print(f'O maior número foi: {max(sorteio)}')