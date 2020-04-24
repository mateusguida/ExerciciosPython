import os
os.system("cls") #limpa janela terminal antes da execução

nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))

media = (nota1+nota2)/2

print("Tirando {} e {}, a média do aluno é {}{}{}".format(nota1, nota2, '\033[35m', media, '\033[m'))


if media < 5.0:
    print('O aluno está {}REPROVADO{}'.format('\033[31m', '\033[m'))

elif media >= 7.0:
    print('O aluno está {}APROVADO{}'.format('\033[32m', '\033[m'))

else:
    print('O aluno está em {}RECUPERAÇÃO{}'.format('\033[33m', '\033[m'))