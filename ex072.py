import os
os.system("cls") #limpa janela terminal antes da execução

lista = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')

while True:
    num = int(input('Digite um número entre 0 e 10: '))
    if 0 <= num <= 10:
        break

print(f'{num} por extenso é {lista[num]}')