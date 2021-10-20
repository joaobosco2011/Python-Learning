numeros = []
opcao = ''
valor = ''

while opcao != 'n':
    valor = int(input('Digite um número: '))
    if numeros.count(valor) >= 1:
        print('Valor duplicado.')
    else:
        numeros.append(valor)
    opcao = (str(input('Você deseja continuar[S/N]? '))).lower().strip()[0]

numeros.sort()
print(f'A lista de números digitada é {numeros}.')
