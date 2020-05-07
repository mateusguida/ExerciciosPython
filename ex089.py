import os
os.system("cls") #limpa janela terminal antes da execução

aluno = list()
turma = list()

while True:
    aluno.append(str(input("Nome: ")))
    aluno.append(float(input("Nota 1: ")))
    aluno.append(float(input("Nota 2: ")))

    turma.append(aluno[:])
    aluno.clear()

    op = str(input("Quer continuar? [S/N] "))
    if op in 'nN':
        break

print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 30)

for i, a in enumerate(turma):
    media = (a[1] + a[2]) / 2
    print(f'{i:<4}{a[0]:<10}{media:>8.2f}')

while True:
    print('-' * 30)
    op = int(input("Mostrar notas de qual aluno? (999 interrompe): "))
    if op == 999:
        break
    else:
        print(f'Notas de {turma[op][0]} são [{turma[op][1]}, {turma[op][2]}]')

print("FINALIZANDO...")
print("<<< VOLTE SEMPRE >>>")
print()