from math import sin, cos, tan, radians

ang = float(input("Digite um ângulo: "))

angr = radians(ang)

print(f'O seno de {ang} é {sin(angr):.2f}')
print(f'O cosseno de {ang} é {cos(angr):.2f}')
print(f'A tangente de {ang} é {tan(angr):.2f}')