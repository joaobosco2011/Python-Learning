idade = 0
sexo = ''
opcao = ''
cont_18 = 0
cont_homem = 0
cont_mulher_20 = 0
while True:
    print('-----CADASTRO DE PESSOAS-----')
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'mf':
        sexo = str(input('Sexo [M/F]: ')).strip().lower()[0]
    opcao =' '
    while opcao not in 'sn':
        opcao = str(input('Quer continuar [S/N]? ')).strip().lower()[0]
    if idade > 18:
        cont_18 = cont_18 + 1
    if sexo == 'm':
        cont_homem = cont_homem + 1
    if sexo == 'f':
        if idade < 20:
            cont_mulher_20 = cont_mulher_20 + 1
    print('------------------------------')
    if opcao == 'n':
        break
print(f'Tem(os) {cont_18} pessoa(s) com mais de 18 anos.')
print(f'Tem(os) {cont_homem} homens cadastrados.')
print(f'E tem(os) {cont_mulher_20} mulher(es) com menos de 20 anos.')
