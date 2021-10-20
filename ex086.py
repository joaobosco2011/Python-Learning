matriz = [ [[], [], []],   [[], [], []],   [[], [], []]]
valor = ''

for i in range(0, 3):

    for c in range(0, 3):
        valor = int(input(f'Digite um valor na posição [{i}, {c}]: '))
        matriz[i][c].append(valor)

print('=-' * 20)
for d in range(0, 3):
    print(matriz[d])
