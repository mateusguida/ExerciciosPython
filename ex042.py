import os
os.system("cls") #limpa janela terminal antes da execução

a = int(input("Primeiro segmento: "))
b = int(input("Segundo segmento: "))
c = int(input("Terceiro segmento: "))

if a < b + c and b < a + c and c < b + a:
    if a == b == c:
        print('Os segmentos acima PODEM FORMAR um triângulo {}EQUILATERO{}'.format('\033[32m','\033[m'))
    elif a == b or b == c or a == c:
        print('Os segmentos acima PODEM FORMAR um triângulo {}ISOSCELES{}'.format('\033[32m','\033[m'))
    else:
        print('Os segmentos acima PODEM FORMAR um triângulo {}ESCALENO{}'.format('\033[32m','\033[m'))
else:
    print('Os segmentos {}NÃO PODEM FORMAR{} um triângulo'.format('\033[31m', '\033[m'))