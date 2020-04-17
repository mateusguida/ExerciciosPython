nome = str(input("Digite o nome completo")).strip()

print(nome.upper())
print(nome.lower())

print(f"Total de letras: {len(nome) - nome.count(' ')}")

nome = nome.split()
print(f'Total de letras do primeiro nome {nome[0]}: {len(nome[0])}')

#Outra opção
#print(f"{nome.find(' ')")


