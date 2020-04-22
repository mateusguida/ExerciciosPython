print("-=-" * 10)
print("Analisador de Triângulos")
print("-=-" * 10)

a = int(input("Primeiro segmento: "))
b = int(input("Segundo segmento: "))
c = int(input("Terceiro segmento: "))

if (a + b) > c and (a + c) > b and (b + c) > a:
    print("Os segmentos acima PODEM FORMAR triângulo")
else:
    print("Os segmentos acima NÃO PODEM FORMAR triângulo")