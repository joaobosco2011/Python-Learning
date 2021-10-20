n1 = n2 = n3 = n4 = 0
numeros = ()
cont_nove = 0

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite um segundo valor: '))
n3 = int(input('Digite um terceiro valor: '))
n4 = int(input('Digite um quarto valor: '))
numeros = (n1, n2, n3, n4)

print(f'O número nove apareceu {numeros.count(9)} vezes.')
if 3 in numeros:
    print(f'O número 3 apareceu na posição {numeros.index(3) + 1}.')
else:
    print('O número 3 não foi encontrado.')
print('Os valores a seguir são números pares: ', end= ' ')
for i in range (0, len(numeros)):
    if numeros[i] % 2 == 0:
        print(numeros[i], end= ' ')
