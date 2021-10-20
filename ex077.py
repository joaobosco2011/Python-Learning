palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR',
            'MERCADO', 'PROGRAMADOR', 'FUTURO')

nome = ''  # variável que irá receber cada palavra da tupla
for n in palavras:
    nome = n.lower()
    print(f'\n Na palavra {n} temos as seguintes vogais: ', end= '')
    for i in nome:
        if i in 'aáàãâeéêèiíìîoóòõôuúùû':  # lista de vogais com e sem acento que serão avaliadas
            print(i, end= ' ')
