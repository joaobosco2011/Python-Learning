from random import randint
computador = randint (1, 10)  # opção randomica entre 1 e 10 que o computador irá jogar
jogador = int(input('Digite um valor entre 1 e 10: '))  # opção entre 1 e 10 que o jogador irá escolhar
par_ou_impar = str(input('Par ou Ímpar [P/I]: ')).strip().upper()[0]  # opção entre PAR ou IMPAR que o jogador irá escolher
resultado = ''

cont = 0
while True:
    total = computador + jogador
    if total % 2 == 0:  # soma sendo par
        resultado = 'P'
    else:  # soma sendo impar
        resultado = 'I'
    if resultado == par_ou_impar:  # o jogador venceu a partida
        cont = cont + 1
        print(f'Você jogou {jogador} e o computador {computador}. O total foi {total}')
        print('Você venceu, vamos jogar novamente.')
    else:  # o jogador perdeu a partida
        break  # função para interromper o loop
    computador = randint(1, 10)
    jogador = int(input('Digite um valor entre 1 e 10: '))
    par_ou_impar = str(input('Par ou Ímpar [P/I]: ')).strip().upper()[0]
print(f'Você jogou {jogador} e o computador {computador}. O total deu {total}')
print(f'Você perdeu e conseguiu ganhar {cont} vez(es).')


