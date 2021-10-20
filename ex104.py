def LeiaInt(msg):
    n = str(input(msg))
    valor = 0

    while True:
        if n.isnumeric():
            valor = int(n)
            break
        else:
            print('ERRO! Digite novamente somente números inteiros.')
            n = str(input('Digite um número inteiro: '))
    
    return valor

# PROGRAMA PRINCIPAL
dado = LeiaInt('Digite um número inteiro: ')
print(f'Você acabou de digitar o número {dado}.')