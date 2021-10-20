numeros = list()  # lista que irá guardar os números digitados pelo usuário
menor = 0  # variável que guardará o menor valor
maior = 0  # variável que guardará o maior valor

for i in range (0, 5):  # parâmetro for para cinco interações
    numeros.append(int(input(f'Digite o {i + 1}º número: ')))  # parâmetro que adiciona elementos ao final de uma lista
    if i == 0:  # avalia se o for está na primeira interação e guarda o primeiro valor dentro da variável menor
        menor = numeros[0]
    if numeros [i] < menor:  # avalia se o valor na interação i é menor que o valor dentro da variável menor
        menor = numeros[i]
    if numeros [i] > maior:  # avalia se o valor na interação i é maior que o valor dentro da variável maior
        maior = numeros[i]

print(f'Você digitou os valores {numeros}.')

print(f'O maior valor digitado foi {maior} nas posições ', end='')
for c in range(0, 5):
    if numeros[c] == maior:
        print(f'{c}...', end='')

print(f'\nO menor valor digitado foi {menor} nas posições ', end='')
for c in range(0, 5):
    if numeros[c] == menor:
        print(f'{c}...', end='')
