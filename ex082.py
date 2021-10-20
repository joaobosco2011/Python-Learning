numeros = list ()  # lista que irá guardar o números digitados pelo usuário
pares = list()  # lista que irá guardar os números pares
impares = list()  # lista que irá guardar os números impares
opcao = ''  # variável que irá ser a opção de continuar ou não
valor = 0  # variável que irá guardar o valor digitado pelo usuário

while opcao != 'n':
    valor = int(input('Digite um número: '))
    opcao = str(input('Deseja continuar [S/N]? ')).strip().lower()[0]
    numeros.append(valor)

    if valor % 2 == 0:  # avalia se o número digitado é par e guarda na lista PAR
        pares.append(valor)
    else:  # avalia se o número digitado é impar e guarda na lista IMPAR
        impares.append(valor)

print(f'A lista completa é {numeros}.')
print(f'A lista de valores pares é {pares}.')
print(f'A lista de valores impares é {impares}.')
