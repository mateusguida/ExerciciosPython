import os
os.system("cls") #limpa janela terminal antes da execução

print('=' * 27)
print("    10 TERMOS DE UMA PA   ")
print('=' * 27)

a = int(input("Primeiro termo: "))
r = int(input("Razão: "))

c = 0
while c < 10:
    print(f"{a}", end=' -> ')
    a += r
    c += 1

print("FIM")