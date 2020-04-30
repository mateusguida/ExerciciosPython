import os
os.system("cls") #limpa janela terminal antes da execução

print('-'*40 + f'\n{"LISTAGEM DE PREÇOS":^40}\n' + '-'*40)
material = ('Lápis', 1.75,
         'Borracha', 2,
         'Caderno', 15,
         'Estojo', 25,
         'Transferidor', 4.2,
         'Compasso', 9.99,
         'Mochila', 120.32,
         'Canetas', 22.30,
         'Livro', 34.90)

for n in range(0, len(material)):
    if n % 2 == 0:
        print(f'{material[n]:.<30}', end='')
        print(f'R$ ', end='')
    else:
        print(f'{int(material[n]):>7.2f}')
print('-'*40)