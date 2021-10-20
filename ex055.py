maior = 0
menor = 0

peso = float(input('Informe o peso da 1ª pessoa: '))
menor = peso

for c in range(2, 6):
    peso = float(input(f'Informe o peso da {c}ª pessoa: '))

    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso

print(f'O maior peso informado foi de {maior}kg.')
print(f'O menor peso informado foi de {menor}kg.')
