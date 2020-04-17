frase = str(input("Digite uma frase: ")).strip()

print(f"A letra A aparece {frase.lower().count('a')} vezes na frase.")
print(f"A primeira letra A aparece na posição {frase.lower().find('a')+1}.")
print(f"A última letra A aparece na posição {frase.lower().rfind('a')+1}.")