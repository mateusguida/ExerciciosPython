preco = float(input('Qual é o preço do seu produto? R$'))

print(f'O produto que custava R${preco:.2f}, na promoção com desconto de 5% vai custar R${preco-preco*0.05:.2f}.')

'''
# Uma segunda opção para esse cálculo

print(f'O produto que custava R${preco:.2f}, na promoção com desconto de 5% vai custar R${preco*0.95:.2f}.')
'''