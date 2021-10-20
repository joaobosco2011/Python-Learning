def ficha(jog = '<desconhecido>', gol = 0):
    print(f'O jogador {jog} marcou {gol} gol(s) no campeonato.')


# PROGRAMA PRINCIPAL

n = str(input('Nome do jogador: '))
g = str(input('Número de gols: '))

if g.isnumeric():
    g = int(g)
else:
    g = 0

if n.strip() == '':
    ficha(gol = g)
else:
    ficha(n, g)
