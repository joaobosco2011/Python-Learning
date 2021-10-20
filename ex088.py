from random import randint
resp = ''

resp = int(input('Quantos jogos você quer que eu sorteie? '))

for i in range(0, resp):
    jogo =  [randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60)]
    print(f'Jogo {i + 1}: {jogo}')
