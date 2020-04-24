import os
os.system("cls") #limpa janela terminal antes da execução

n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))

if n1 > n2:
    print('O {}PRIMEIRO{} valor é maior'.format('\033[35m','\033[m'))
elif n2 > n1:
    print('O {}SEGUNDO{} valor é maior'.format('\033[35m','\033[m'))
else:
    print('Não existe valor maior, os dois são {}IGUAIS{}'.format('\033[35m','\033[m'))


