sal = int(input("Qual o salário do funcionário? R$ "))

if sal > 1250:
    aum = sal * 1.1
else:
    aum = sal * 1.15

print(f'QUem ganhava R$ {sal:.2f} passa a ganhar R$ {aum:.2f} agora.')