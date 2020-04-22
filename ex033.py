n1 = int(input("Primeiro valor: "))
maior = n1
menor = n1

n2 = int(input("Segundo valor: "))

if n2 > maior:
    maior = n2
if n2 < menor:
    menor = n2

n3 = int(input("Terceiro valor: "))

if n3 > maior:
    maior = n3
if n3 < menor:
    menor = n3
    
print(f'O menor valor digitado foi {menor}')
print(f'O maior valor digitado foi {maior}')

