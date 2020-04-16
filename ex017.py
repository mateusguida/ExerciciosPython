from math import sqrt, pow, hypot

co = float(input("Digite o comprimento do cateto oposto: "))

ca = float(input("Digite o comprimento do cateto adjacente: "))

hipo = hypot(co, ca)

'''
# Outra versão 1

hipo = sqrt( pow(co,2) + pow(ca,2) )

# Outra versão 2
hipo = (co ** 2 + ca ** 2) ** (1/2)
'''


print(f'A hipotenusa é {hipo}')