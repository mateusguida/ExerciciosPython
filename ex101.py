def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    if idade < 16:
        print(f'Com {idade} anos: NÃO VOTA')
    elif 16 <= idade < 18 or idade > 65:
        print(f'Com {idade} anos: OPCIONAL')
    else:
        print(f'Com {idade} anos: OBRIGATÓRIO')


def limpa():
    import os
    os.system("cls") #limpa janela terminal antes da execução

limpa()
nasc = int(input("Em que ano você nasceu? "))
voto(nasc)
