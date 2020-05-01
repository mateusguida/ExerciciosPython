import os
os.system("cls") #limpa janela terminal antes da execução


expr = str(input(f"Digite uma expressão: "))
pilha = []

for simb in expr:
    if simb == "(":
        pilha.append("(")
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print("Sua expressão está correta !")
else:
    print("Sua expressão está incorreta !")

# Outra opção
'''
p1 = expr.count("(")
p2 = expr.count(")")
if p1 == p2:
    print("Sua expressão está correta !")
else:
    print("Sua expressão está incorreta !")
'''

print('-=' * 30)
print(f'{expr}')