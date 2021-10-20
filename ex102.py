def fatorial (n):
    print('-' * 27)
    fat = 1

    for i in range(0, n):
        if i != (n - 1): ## avalia se a variável i não está na última iteração
            print(f'{i + 1}', end= ' x ')
        else:
            print(f'{i + 1}', end= ' = ')
        fat = fat * (i + 1)

    """
    fatorial(n)
        -> Cálcula o fatoria de um número.
        -> parâmetro n: número a ser cálculado o fatorial
        -> return: o valor de fatorial do número n
    """
    print(fat)



## PROGRAMA PRINCIPAL
fatorial(5)
help(fatorial)