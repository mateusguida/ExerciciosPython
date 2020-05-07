import os
os.system("cls") #limpa janela terminal antes da execução

jog = dict()
gols = list()

jog["nome"] = str(input("Nome do jogador: "))
jog["partidas"] = int(input(f'Quantas partidas {jog["nome"]} jogou? '))
jog["total"] = 0

for c in range(0, jog["partidas"]):
    gols.append(int(input(f"   Quantos gols na partida {c}? ")))
    jog["total"] += gols[c]

jog["gols"] = gols

print('-=' * 30)
print(jog)

print('-=' * 30)
for k, v in jog.items():
    print(f'O campo {k} tem o valor {v}')

print('-=' * 30)
print(f'O jogador {jog["nome"]} jogou {jog["partidas"]} partidas.')
for i, v in enumerate(jog["gols"]):
    print(f'    => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jog["total"]} gols.')


print()