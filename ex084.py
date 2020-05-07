import os
os.system("cls") #limpa janela terminal antes da execução


pessoas = list()
dados = list()

while True:
    dados.append(str(input("Nome: ")).strip())
    dados.append(float(input("Peso: ")))
    
    if len(pessoas) == 0:
        menor = maior = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        elif dados[1] < menor:
            menor = dados[1]
    
    pessoas.append(dados[:])
    dados.clear()
    
    resp = str(input("Quer continuar? [S/N] "))
    if resp in 'nN':
        break

print('-=' * 30)
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi de {maior:.2f}. Peso de ', end='')
for c in pessoas:
    if c[1] == maior:
        print(f'[{c[0]}] ', end='')

print()
print(f'O menor peso foi de {menor:.2f}. Peso de ', end='')
for c in pessoas:
    if c[1] == menor:
        print(f'[{c[0]}] ', end='')