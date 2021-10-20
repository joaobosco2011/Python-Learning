def contador():
    n = 1
    c = 10
    ## contagem de 1 até 10 de 1 em 1
    print('-=' * 15)
    print('Contagem de 1 até 10 de 1 em 1!')
    for i in range(0, 10):
        print(n, end= " ")
        n = n + 1
    print(' ')
    print('-=' * 15)


    ## contagem de 10 até 0  de 2 em 2
    print('Contagem de 10 até 0 de 2 em 2!')
    for i in range(0, 6):
        print(c, end= " ")
        c = c - 2
    print(' ')
    print('-=' * 15)


    ## contagem aleatória
    incio = int(input('Início: '))
    fim = int(input('Fim: '))
    passo = abs(int(input('Passo: ')))
    
    print('-=' * 15)
    print(f'Contagem de {incio} até {fim} de {passo} em {passo}!')
    
    ## variável inicio maior que a variável fim
    
    while incio > fim:
        print(incio, end= ' ')
        incio = incio - passo
    print(' ')


    ## variável fim maior que o inicio
    while fim > incio:
        print(incio, end=' ')
        incio = incio + passo
    print(' ')

        
contador()
