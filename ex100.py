from random import randint
numeros = list()

def sorteia():
    for i in range(0, 5):
        numeros.append(randint(0, 9))
    print(f'Sorteando 5 valores da lista:', end=" ")
    
    for d in range(0, len(numeros)):
        print(numeros[d], end=' ')
    print(' ')


def somaPar():
    soma = 0
    for c in range(0, len(numeros)):
        if numeros[c] % 2 == 0:
            soma = soma + numeros[c]
    print(f'A soma dos números pares da lista é {soma}.')

sorteia()
somaPar()