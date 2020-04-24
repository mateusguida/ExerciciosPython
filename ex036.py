valor = int(input("Valor da casa: R$ "))
sal = int(input("Salário do comprador: R$ "))
ano = int(input("Quantos anos de financiamento? "))

prest = valor / (ano*12)

print(f'Para pagar uma casa de R$ {valor} em {ano} anos a prestação será de R$ {prest:.2f}')

if prest > sal*0.3:
    print('Empréstimo {}NEGADO{}'.format('\033[31m','\033[m'))
else:
    print('Empréstimo pode ser {}CONCEDIDO{}'.format('\033[32m','\033[m'))