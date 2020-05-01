import os
os.system("cls") #limpa janela terminal antes da execução

print('-'*40 + f'\n{"LISTAGEM DE PREÇOS":^40}\n' + '-'*40)
palavras = ('Lapis','Borracha','Caderno','Estojo','Transferidor',
         'Compasso','Mochila','Canetas','Livro')

for p in palavras:

    print(f'\nNa palavra {p.upper()} temos ', end='')

    for c in p:
        if c.lower() in 'aeiou':
            print(f'{c.lower()} ', end='')