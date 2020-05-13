def titulo(txt):
    tam = len(txt) + 4
    print('~' * (tam))
    print(f'  {txt}')
    print('~' * (tam))

def limpa():
    import os
    os.system("cls") #limpa janela terminal antes da execução


limpa()
titulo("Mateus Guida")
titulo("Curso de Python")
titulo("CeV")
