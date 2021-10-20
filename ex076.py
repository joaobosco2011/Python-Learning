produtos = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.9, 'Estojo', 25, 'Transferidor', 4.2, 'Compasso', 9.99,
            'Mochila', 120.32, 'Canetas', 22.3, 'Livro', 34.9)
total = 0
print('-' * 40)
print(f'{"LISTA DE PREÇOS":^40}')
print('-' * 40)
for i in range(0, len(produtos)):
    if i % 2 == 0:
        print(f'{produtos[i]:.<30}', end='')
    else:
        print(f'R$ {produtos[i]:.2f}')
        total = total + produtos[i]
print(' ')
print(f'{"TOTAL":.<30}', end='')
print(f'R$ {total:.2f}')
