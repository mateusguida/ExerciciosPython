import os
os.system("cls") #limpa janela terminal antes da execução

from datetime import date

nasc = int(input("Ano de nascimento: "))
ano = date.today().year
ano = 2017
idade = ano - nasc

print(f'O atleta tem {idade} anos.')

if idade <= 9:
    print('Classificação: {}MIRIM{}'.format('\033[36m','\033[m'))
elif idade <= 14:
    print('Classificação: {}INFANTIL{}'.format('\033[36m','\033[m'))
elif idade <= 19:
    print('Classificação: {}JUNIOR{}'.format('\033[36m','\033[m'))
elif idade <= 25:
    print('Classificação: {}SENIOR{}'.format('\033[36m','\033[m'))
else:
    print('Classificação: {}MASTER{}'.format('\033[36m','\033[m'))
