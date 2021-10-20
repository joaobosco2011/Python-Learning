from random import randint
numeros = (randint(1, 5), randint(1, 5), randint(1, 5), randint(1, 5), randint(1, 5))
print(f'A lista de números é {numeros}.')
menor = sorted(numeros)
maior = sorted(numeros)
print(f'O menor número da lista é {menor[0]}.')
print(f'O maior número da lista é {maior[-1]}.')
