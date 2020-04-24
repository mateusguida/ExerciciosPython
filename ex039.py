import os
os.system("cls") #limpa janela terminal antes da execução

from datetime import date

nasc = int(input("Ano de nascimento: "))
anoatual = date.today().year
idade = anoatual-nasc
anoalist = nasc + 18

print("Quem nasceu em {} tem {}{}{} anos em {}".format(nasc, '\033[34m', idade, '\033[m', anoatual))

if idade > 18:
    print("Você já deveria ter se alistado há {} anos".format(anoatual - anoalist))
    print("Seu alistamento foi em {}{}{}".format('\033[31m', anoalist, '\033[m'))

elif idade < 18:
    print("Ainda faltam {} anos para o alistamento".format(anoalist - anoatual))
    print("Seu alistamento será em {}{}{}".format('\033[31m', anoalist, '\033[m'))

else: # idade = 18
    print("Você tem que se alistar {}IMEDIATAMENTE{}".format('\033[31m', '\033[m'))