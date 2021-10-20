jogador = dict() ## dicionário que vai receber os dados de cada jogador
cadastro = list() ## lista que vai guardar os dicionários com os dados dos jogadores
opcao = 's' ## variável que guarda S ou N caso o usuário queira ou não continuar
partidas = 0 ## variável que vai guardar o número de partidas de cada jogador
lista_gols = list() ## lista que guardará os gols para somar futuramente
opcao_dados = 0 ## variável para escolher o jogador que terá os seus dados mostrados

## CADASTRO DOS JOGADORES E SEUS GOLS
while opcao in 'Ss':
    jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas o {jogador["nome"]} jogou? '))

    for i in range(0, partidas):
        lista_gols.append(int(input(f'Quantos gols na partida {i + 1}? ')))

    jogador['gols'] = lista_gols[:]

    jogador['total'] = sum(lista_gols)

    cadastro.append(jogador.copy())

    lista_gols.clear()

    opcao = str(input('Deseja continuar [S/N]? ')).strip()

print('-' * 45)
print(f'{"Cod":^2}  {"Nome":^10}    {"Gols":^10}    {"Total":^10}'   )
print('-' * 45)

## IMPRIME A TABELA COM OS JOGADORES E SEUS GOLS
for d in range(0, len(cadastro)):
    print(f'{d + 1}     {str(cadastro[d]["nome"]):<10}   {str(cadastro[d]["gols"]):<15}   {str(cadastro[d]["total"]):^5}')

print('-' * 45)

## MOSTA OS DADOS DE UM JOGADOR ESPECÍFICO ESCOLHIDO PELO USUÁRIO
print('-' * 45)
while True:
    opcao_dados = int(input('Mostrar dados de qual jogador (999 para parar)? '))
    if opcao_dados == 999:
        break
    else:
        if opcao_dados > len(cadastro):
            print(f'ERRO! A opção {opcao_dados} não é válida.')
        else:
            opcao_dados = opcao_dados - 1
            print('-' * 45)
            print(f'    LEVANTAMENTO DO JOGADOR {cadastro[opcao_dados]["nome"]}')
            for j, g in enumerate(cadastro[opcao_dados]["gols"]):
                print(f'No jogo {j + 1} fez {g} gols.')
            
    