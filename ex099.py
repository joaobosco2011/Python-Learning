def maior_valor(*num):
    maior = ""
    print('=' * 50)
    print('Analisando os valores passados...')
    print(f'{num} foram informados {len(num)} valores ao todo.')

    # avaliando se a função está vazia
    if num == '':
        print(f'{0} foram informados {0} valores ao todo.')
        print(f'O maior valor informado foi {0}.')
    # vai avaliar qual dos valores informados é o maior
    for c in range(0, len(num)):
        if c == 0:
            maior = num[c]
        
        if num[c] > maior:
            maior = num[c]

   
    print(f'O maior valor informado foi {maior}.')
    print('=' * 50)


maior_valor(1, 2, 5, 8)

maior_valor(2, 9, 4, 5, 7, 1)

maior_valor(4, 7, 0)

maior_valor(1, 2)

maior_valor(6)

maior_valor()