times = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico Paranaense', 'São Paulo', 'Internacional', 'Corinthians',
         'Fortaleza', 'Goiás', 'Bahia', 'Vasco', 'Atlético', 'Fluminense', 'Botafogo', 'Ceará', 'Cruzeiro', 'Csa',
         'Chapecoense', 'Avaí')
print('Os cinco primeiros colocados do Brasileirão de 2019')
for i in range(0, 5):
    print(f'O {i + 1}º colocado é o {times[i]}.')
print(' ')

print('Os quatro ultimos colocados do Brasileirão de 2019')
for i in range(0, 4):
    print(f"O {20 - i}º colocado é o {times[-i -1]}.")
print(' ')

print('Os times listados em ordem alfabética.')
print(sorted(times))
print(' ')

print(f'A posição da Chapecoense é {times.index("Chapecoense") + 1}º lugar no campeonato brasileiro.')
