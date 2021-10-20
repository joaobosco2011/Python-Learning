numero = list()
pares = list ()
impares = list()
n = 0

for i in range(0, 7):
    n = int(input(f'Digite o {i + 1}º valor: '))

    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    
numero.append(pares[:])
numero.append(impares[:])

numero[0].sort()
numero[1].sort()

print(f'Os valores pares digitados foram {numero[0]}.')
print(f'Os valores impares digitados foram {numero[1]}.')
