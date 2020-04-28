import os
os.system("cls") #limpa janela terminal antes da execução

print('=' * 27)
print("    10 TERMOS DE UMA PA   ")
print('=' * 27)

a = int(input("Primeiro termo: "))
r = int(input("Razão: "))

cExt = termos = 10
while cExt != 0:
    cInt = int(0)
    while cInt < cExt:
        print(f"{a}", end=' -> ')
        a += r
        cInt += 1
    print("PAUSA")
    cExt = int(input('Quantos termos mais você quer exibir? '))
    termos += cExt

print(f'Progressão finalizada com {termos} termos mostrados.')