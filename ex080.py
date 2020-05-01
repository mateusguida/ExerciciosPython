import os
os.system("cls") #limpa janela terminal antes da execução

valores = []
for c in range(0,5):
    num = int(input(f"Digite um valor: "))
    if c == 0 or num > valores[-1]:
        valores.append(num)
        print("Adicionado ao final da lista...")
    else:
        pos = 0
        while pos < len(valores):
            if num <= valores[pos]:
                valores.insert(pos,num)
                print(f'O valor {num} foi adicionado na posição {pos} da lista...')
                break
            pos += 1
        
print('-=' * 30)
valores.sort()
print(f'Você digitou os valores {valores}')