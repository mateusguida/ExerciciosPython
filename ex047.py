import os
os.system("cls") #limpa janela terminal antes da execução

for c in range(0, 51, 2):
    print(c, end=' ')
print('{}Acabou{}'.format('\033[32m', '\033[m'))

