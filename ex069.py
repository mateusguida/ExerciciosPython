import os
os.system("cls") #limpa janela terminal antes da execução

tot = mulher = homem = 0

while True:
    print("-" * 20)
    print(f'CADASTRE UMA PESSOA')
    print("-" * 20)
    
    idade = int(input("Idade: "))
    if idade > 18:
        tot += 1
    
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input("Sexo [M/F]: ")).strip().upper()[0]

    if sexo == 'M':
        homem += 1
    else:
        if idade < 20:
            mulher += 1
    
    op = ' '
    while op not in 'SN':
        op = str(input("Quer continuar? [S/N]")).strip().upper()[0]
    
    if op == 'N':
        break

print('~' * 20)
print(f'Total de pessoas com mais de 18 anos: {tot}')
print(f'Ao todo temos {homem} homens cadastrados')
print(f'E temos {mulher} mulheres com menos de 20 anos')