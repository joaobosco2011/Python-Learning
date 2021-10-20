matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
valor = ''
soma = 0
n_par = 0
soma_terceira_coluna = 0
maior = 0

for i in range(0, 3): #  linha da matriz
    for c in range(0, 3): #  coluna da matriz
        valor = int(input(f'Digite um valor na posição [{i}, {c}]: '))
        matriz[i][c] = valor
        
## impressão da matriz
print('=-' * 20)
for d in range(0, 3):
    print(matriz[d])

## soma dos valores pares
for i in range (0, 3):  # linha da matriz
    for c in range(0, 3):  # coluna da matriz
        if matriz[i][c] % 2 == 0:
            soma = soma + matriz[i][c]

print('=-' * 20)
print(f'A soma dos elementos pares é {soma}.')

## soma dos valores da terceira coluna
for i in range(0, 3):
    soma_terceira_coluna = soma_terceira_coluna + matriz[i][2]

print(f'A soma dos valores da terceira coluna é {soma_terceira_coluna}.')

## o maior valor da segunda linha
for i in range (0, 3):
    if matriz[1][i] > maior:
        maior = matriz[1][i]

print(f'O maior valor da segunda linha é {maior}.')