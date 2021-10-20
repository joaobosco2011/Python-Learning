print('-' * 20)
soma = 0
cont_1000 = 0
produto_mais_barato = ''
valor_do_produto_mais_barato = 0
cont = 0
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço R$ '))
    soma = soma + preco
    if preco > 1000:
        cont_1000 = cont_1000 + 1
    cont = cont + 1
    if cont == 1:
        produto_mais_barato = produto
        valor_do_produto_mais_barato = preco
    if preco < valor_do_produto_mais_barato:
        valor_do_produto_mais_barato = preco
        produto_mais_barato = produto
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Adicionar um novo produto [S/N]? ')).strip().upper()[0]
    if opcao == 'N':
        break
    print('-' * 20)
print('{:-^30}'.format('FIM'))
print(f'O valor total do seu carrinho é de R$ {soma:.2f}.')
print(f'Tem(os) {cont_1000} produto(s) acima de R$ 1.000,00.')
print(f'O produto mais barato é {produto_mais_barato} e o seu valor é R$ {valor_do_produto_mais_barato:.2f}.')




