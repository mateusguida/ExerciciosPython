import os
os.system("cls") #limpa janela terminal antes da execução

from time import sleep

for c in range(10, -1, -1):
    print(c)
    sleep(0.5)

print('{}BUM! BUM! POOOW! {}'.format('\033[31m', '\033[m'))

