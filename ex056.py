import os
os.system("cls") #limpa janela terminal antes da execução

media = 0
qtd = 0

for c in range(1,5):
    print(f'\n----- {c}ª PESSOA -----')
    nome = str(input("Nome: ")).strip()
        
    idade = int(input("Idade: "))
    media += idade

    sexo = str(input("Sexo [M/F]: ")).strip().upper()

    if sexo == 'M':
        if c == 1:
            velho = nome
            idvelho = idade
        else:
            if idade > idvelho:
                idvelho = idade
                velho = nome
    else:
        if idade < 20:
            qtd += 1


print(f'\nA média de idade do grupo é de {media/5:.1f} anos.')
print(f'O homem mais velho tem {idvelho} e se chama {velho}.')
print(f'Ao todo são {qtd} mulheres com menos de 20 anos.')

