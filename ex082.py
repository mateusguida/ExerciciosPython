import os
os.system("cls") #limpa janela terminal antes da execução

valores = []
valorespar = []
valoresimpar = []
while True:
    valores.append(int(input(f"Digite um valor: ")))
    flag = str(input("Quer continuar? [S/N]")).lower()
    if flag == 'n':
        break
        
print('-=' * 30)
print(f'A lista completa é: {valores}')

for c in valores:
    if c % 2 == 0:
        valorespar.append(c)
    else:
        valoresimpar.append(c)

print(f'A lista de pares é: {valorespar}')
print(f'A lista de ímpares é: {valoresimpar}')