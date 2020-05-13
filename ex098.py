def contagem(ini, passo, fim):
    print('-=' * 20)
    print(f'Contagem de {ini} até {fim} de {passo} em {passo}')
    if ini < fim:
        for i in range(ini, fim+1, passo):
            print(f'{i} ', end='')
    else:
        passo *= -1
        for i in range(ini, fim-1, passo):
            print(f'{i} ', end='')
    print("FIM!")

def limpa():
    import os
    os.system("cls") #limpa janela terminal antes da execução

limpa()
contagem(1,1,10)
contagem(10,2,0)
print('Agora é a sua vez de personalizar a contagem')
inicio = int(input("Início: "))
final = int(input("Fim: "))
contador = int(input("Passo: "))
contagem(inicio, contador, final)
print()
