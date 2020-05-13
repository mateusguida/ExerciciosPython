def area(l,c):
    res = l * c
    print(f"A área de um terreno {l:.1f} x {c:.1f} é de {res:.1f} m².")

def limpa():
    import os
    os.system("cls") #limpa janela terminal antes da execução


limpa()
print(" Controle de Terrenos")
print('-' * 20)
largura = float(input("LARGURA (m): "))
comprim = float(input("COMPRIMENTO (m): "))
area(largura, comprim)

