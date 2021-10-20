pessoa = dict() # dicionário para receber os dados de cada pessoa
cadastro = list() # lista que irá guardar a cada iteração os dados que estão no dicionário 'pessoa'
opcao = 's' # variável para o usuário escolher se continua ou não
media = 0 # variável para cálculo da média
soma_idade = 0 # variável para o cálculo da soma das idades de cada pessoa cadastrada
cont = 0 # variável que irá contar o número de mulheres

## função 'while'' que armazena os dados de cada pessoa cadastrada no dicionário e na lista
while opcao in 'Ss':
    pessoa['nome'] = str(input('Nome: '))

    pessoa['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()
    while pessoa['sexo'] not in 'MF':
        print('ERRO! Responda apenas M ou F')
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()

    pessoa['idade'] = int(input('Idade: '))

    ## os dados do dicionário 'pessoa' serão copiados para a lista 'cadastro'
    cadastro.append(pessoa.copy())

    ## avalia se o usuário digitou S ou N apenas
    opcao = str(input('Quer continuar [S/N]? ')).strip()
    while opcao not in 'SsNn':
        print('ERRO! Responda apenas S ou N.')
        opcao = str(input('Quer continuar [S/N]? '))

## imprime o total de pessoas cadastradas
print(f'O total de pessoas cadastradas foi de {len(cadastro)}.')

#  cálculo da média de idade das pessoas cadastradas
for i in range(0, len(cadastro)):
    soma_idade = soma_idade + cadastro[i]['idade']  
media = soma_idade / len(cadastro)

print(f'A média de idade é de {media} anos.')

# lista somente com as mulheres
for c in range(0, len(cadastro)):
    if cadastro[c]["sexo"] == 'F':
        print(f'    -> A {cont + 1}ª mulher se chama {cadastro[c]["nome"]}')
        cont = cont + 1

# lista de pessoas coma idade acima da média
print(f'Lista das pessoas com idade acima da média:')
for d in range(0, len(cadastro)):
    if cadastro[d]['idade'] > media:
        print(f'    -> nome = {cadastro[d]["nome"]}; sexo = {cadastro[d]["sexo"]}; idade = {cadastro[d]["idade"]} ')
