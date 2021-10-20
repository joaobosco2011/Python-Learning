numeros = list ()
opcao = ''
valor = 0

while opcao != 'n':
    valor = int(input('Digite um valor: '))
    opcao = str(input('Você deseja continuar [S/N] ? ')).strip().lower()[0]
    numeros.append(valor)

print(f'Você digitou {len(numeros)} numero(s).')

numeros.sort(reverse = True)
print(f'Os números em ordem decrescente são {numeros}')

if 5 in numeros:
    print('O valor 5 foi encontrado na lista!')
else:
    print('O valor 5 não foi encontrado na lista!')
