dist = int(input("Qual é a distância da sua viagem? "))
print(f'Você está prestes a iniciar uma viagem de {dist:.2f} Km.')

if dist <= 200:
    preco = dist * 0.5
else:
    preco = dist * 0.45

# Outra opção, simplificada
# preco = dist * 0.5 if dist <= 200 else dist * 0.45

print(f'E o preço da sua passagem será de R$ {preco:.2f}.')