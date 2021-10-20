numeros = list ()
valor = ''

for i in range(0, 5):
    valor = int(input('Digite um valor: '))
    
    if i == 0:  # primeira iteração
        numeros.append(valor)  # adiciona o valor digitado ao final da lista
    
    if i == 1:  # segunda iteração
        if valor > numeros[-1]:  # avalia se o valor digitado é maior que o número na última posição da lista
            numeros.append(valor)  # adiciona o valor digitado ao final da lista
        else:
            numeros.insert(0, valor)  # insere na posição 0 o valor digitado
    
    if i == 2:  # terceira iteração
        if valor > numeros[-1]:
            numeros.append(valor)
        elif valor < numeros[0]:
            numeros.insert(0, valor)
        else:
            numeros.insert(1, valor)
    
    if i == 3:  # quarta iteração
        if valor > numeros[-1]:
            numeros.append(valor)
        elif valor < numeros[0]:
            numeros.insert(0, valor)
        elif valor < numeros[1]:
            numeros.insert(1, valor)
        else:
            numeros.insert(2, valor)
        
    if i == 4: # última iteração
        if valor > numeros[-1]:
            numeros.append(valor)
        elif valor < numeros[0]:
            numeros.insert(0, valor)
        elif valor < numeros[1]:
            numeros.insert(1, valor)
        elif valor < numeros[2]:
            numeros.insert(2, valor)
        else:
            numeros.insert(3, valor)
    
print(f'Os valores digitados em ordem são {numeros}.')
