metro = float(input("Digite uma distância em metros: "))

print(f'A medida de {metro:.1f} corresponde a')
print(f'{metro/1000:.3f} km')
print(f'{metro/100:.2f} hm')
print(f'{metro/10:.1f} dam')
print(f'{metro*10:.0f} dm')
print(f'{metro*100:.0f} cm')
print(f'{metro*1000:.0f} mm')