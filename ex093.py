cadastro = dict()
gols = list()
tot = 0
gol = 0

cadastro['nome'] = str(input('Nome do Jogador: '))
partidas = 0
partidas = int(input(f'Quantas partidas o jogador {cadastro["nome"]} jogou? '))

for i in range(0, partidas):
    gol = int(input(f'Quantos gols na partida {i + 1}? '))
    gols.append(gol)
    tot = gol + tot

cadastro['gols'] = gols
cadastro['total'] = tot

print('-=' * 30)
print(cadastro)

print('-=' * 30)
print(f'O jogador {cadastro["nome"]} jogou {partidas} partidas.')

for i in range(0, partidas):
    print(f'    => Na partida {i + 1}, fez {cadastro["gols"][i]} gol(s).')

print(f'Fez um total de {tot} gols')