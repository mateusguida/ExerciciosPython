import os
os.system("cls") #limpa janela terminal antes da execução

dados = dict()
pessoas = list()
media = 0

while True:
    dados["nome"] = str(input("Nome: "))

    while True:
        dados["sexo"] = str(input("Sexo: [M/F]: ")).strip()
        if dados["sexo"] not in 'mMfF':
            print("ERRO! Por favor, digite apenas M ou F.")
        else:
            break

    dados["idade"] = int(input("Idade: "))
    media += dados["idade"]

    pessoas.append(dados.copy())
    dados.clear()
    while True:
        op = str(input("Quer continuar? [S/N]: ")).strip()
        if op not in 'sSnN':
            print("ERRO! Responda apenas S ou N.")
        else:
            break

    if op in 'nN':
        break

media /= len(pessoas)
print(pessoas)
print('-=' * 30)
print(f'A) Ao todos temos {len(pessoas)} pessoas cadastradas.')
print(f'B) A média de idade é de {media:.2f} anos.')
print(f'C) As mulheres cadastradas foram ', end='')
for p in pessoas:
    if p["sexo"] in 'fF':
        print(f'{p["nome"]} ', end='')
print()

print(f'D) Lista das pessoas que estão acima da média:')
for p in pessoas:
    if p["idade"] >= media:
        print('   ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print()
print("<< ENCERRADO >>")
print()