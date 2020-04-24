import os
os.system("cls") #limpa janela terminal antes da execução

from datetime import date

for c in range(1,6):
  
    peso = float(input(f"Peso da {c}° pessoa: "))

    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f'O maior peso lido foi de {maior} Kg')
print(f'O menor peso lido foi de {menor} Kg')
