larg = float(input("Largura da parede: "))
alt = float(input("Altura da parede: "))

area = larg * alt

print(f'SUa parede tem a dimensão de {larg:.2f}x{alt:.2f} e sua área é de {area:.3f}m².')
print(f'Para pintar essa parede, você precisará de {area/2} litros de tinta')