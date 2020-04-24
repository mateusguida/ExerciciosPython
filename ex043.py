import os
os.system("cls") #limpa janela terminal antes da execução

peso = float(input("Qual o seu peso? (Kg) "))
altura = float(input("Qual é a sua altura? (m) "))

imc = peso / (altura ** 2)
print(f"O IMC desta pessoa é de {imc:.1f}")

if imc < 18.5:
    print("ABAIXO DO PESO")
elif 18.5 <= imc < 25:
    print("PESO IDEAL")
elif 25 <= imc < 30:
    print("SOBREPESO")
elif 30 <= imc < 40:
    print("OBESIDADE") 
else:
    print("OBESIDADE MÓRBIDA")