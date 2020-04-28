import os
os.system("cls") #limpa janela terminal antes da execução

sexo = str(input("Informe seu sexo: [M/F] ")).strip().upper()[0]

while sexo not in 'MmFf':
    print(sexo)
    sexo = str(input("Dados inválidos. Informe seu sexo: [M/F] ")).strip().upper()[0]

print(f'Sexo {sexo} registrado com sucesso!')
