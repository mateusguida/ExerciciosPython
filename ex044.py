import os
os.system("cls") #limpa janela terminal antes da execução

print('=' * 8 + ' LOJAS GUANABARA ' + '=' * 8 + '\n')

preco = float(input("Preço das compras: R$ "))

print("\nFORMAS DE PAGAMENTO\n")
print("[ 1 ] à vista dinheiro/cheque")
print("[ 2 ] à vista cartão")
print("[ 3 ] 2x no cartão")
print("[ 4 ] 3x ou mais no cartão")
op = int(input("\nQual é a sua opção? "))

if op == 1:
    preco = preco * 0.9
    print(f"O preço à vista no dinheiro/cheque com desconto é de R$ {preco:.2f}")
elif op == 2:
    preco = preco * 0.95
    print(f"O preço à vista no cartão com desconto é de R$ {preco:.2f}")
elif op == 3:
    preco = preco / 2
    print(f"O preço em 2x no cartão será em duas parcelas de R$ {preco:.2f} cada")
elif op == 4:
    preco = preco * 1.2
    parc = int(input("Quantas parcelas? "))
    preco = preco / parc
    print(f"O preço será em {parc} parcelas de R$ {preco:.2f} cada")
    print(f"O preço total com juros é de R$ {preco*parc:.2f}")
else:
    print("Esta opção não existe, escolha com atenção!")