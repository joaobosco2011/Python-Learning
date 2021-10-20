n = int(input('Informe um número não negativo: '))
n_fat = 1  # variável que irá guardar a multiplicação do fatorial
for i in range (1, n+1):
    n_fat = n_fat * i
print(f'O fatorial de {n}! é {n_fat}.')

