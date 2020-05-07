import os
os.system("cls") #limpa janela terminal antes da execução

aluno = dict()

aluno['nome'] = str(input("Nome: "))
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
    
if aluno['média'] > 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'

print('-=' * 20)

for i, v in aluno.items():
    print(f'  - {i} é igual a {v}')
print()