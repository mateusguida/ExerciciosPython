def maior(* num):
    cont = maiorn = 0
    print('-=' * 30)
    print("Analisando os valores passados...")

    for valor in num:
        print(f'{valor} ', end='')
        if cont == 0:
                maiorn = valor
        else:
            if valor > maiorn:
                maiorn = valor
        cont += 1
    
    if cont == 0:
        print("Não foi informado nenhum valor.")
    else:
        print(f'Foram informados {cont} valores ao todo.')
        print(f'O maior valor foi {maiorn}.')
    print()

def limpa():
    import os
    os.system("cls") #limpa janela terminal antes da execução

limpa()
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()

