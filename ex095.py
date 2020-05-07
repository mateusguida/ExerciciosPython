import os
os.system("cls") #limpa janela terminal antes da execução

jog = dict()
gols = list()
time = list()

while True:
    jog["nome"] = str(input("Nome do jogador: "))
    jog["partidas"] = int(input(f'Quantas partidas {jog["nome"]} jogou? '))
    jog["total"] = 0

    for c in range(0, jog["partidas"]):
        gols.append(int(input(f"   Quantos gols na partida {c+1}? ")))
        jog["total"] += gols[c]

    jog["gols"] = gols[:]
    gols.clear()

    time.append(jog.copy())

    while True:
        op = str(input("Quer continuar? [S/N]: "))
        if op in 'nNsN':
            break
        print("Digite S ou N.")

    if op in 'nN':
        break

print('-=' * 40)
print('cod ', end='')
for i in jog.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 55)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print()
while True:
    while True:
        op = int(input("Mostrar dados de qual jogador? (999 para parar): "))
        if 0 <= op < len(time) or op == 999:
            break
        print("Não existe jogador com este código.")

    if op == 999:
        break

    print(f' -- LEVANTAMENTO DO JOGADOR {time[op]["nome"]}')
    for i, v in enumerate(time[op]["gols"]):
        print(f'    No jogo {i+1} fez {v} gols.')

print("<< VOLTE SEMPRE >>")
print()