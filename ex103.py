def ficha(nome="<desconhecido>", gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')

def limpa():
    import os
    os.system("cls") #limpa janela terminal antes da execução

limpa()
n = str(input("Nome do jogador: "))
g = str(input("Número de gols: "))

if g.isnumeric():
    g = int(g)
else:
    g = 0

if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n,g)