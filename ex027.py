nome = str(input("Digite o seu nome completo: ")).strip()

nome = nome.title()
nome = nome.split()

print(f'Primeiro nome: {nome[0]}')
print(f'Último nome: {nome[len(nome)-1]}')