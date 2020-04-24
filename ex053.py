import os
os.system("cls") #limpa janela terminal antes da execução

frase = str(input("Digite uma frase: ")).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]

'''
inverso = junto [::-1]
# mesma coisa, mas sem o FOR
# macete de python
'''
    
print(f'O inverso de {junto} é {inverso}')

if inverso == junto:
    print("Temos um palíndromo!")
else:
    print("A frase digitada não é um palíndromo!")