from random import randint # importação da biblioteca random
from time import sleep  # importação da biblioteca time

computador = randint(0, 2)  # opção aleatória que o computador irá jogar
lista = ['PEDRA', 'PAPEL', 'TESOURA']  # lista com as jogadas

jogador = int(input('''Escolha um opção abaixo.
[0] PEDRA
[1] PAPEL
[2] TESOURA
Sua opção: '''))

if jogador >= 0 and jogador <= 2:
    print(f'O jogador escolheu {lista[jogador]}.')  # impresão da opção escolhida pelo jogador
    print(f'O computador escolheu {lista[computador]}.')  # impressão da opção escolhida pelo computador

    # bloco de código que faz o sleep da tela antes de apresentar a resposta de quem ganhou
    print('*-*-' * 10)
    sleep(1)
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO !!!!!!')
    print('*-*-' * 10)
    sleep(0.5)

    # bloco de código com as condições para determinar quem ganha partida
    if jogador == 0:  # jogador escolher PEDRA
        if computador == 0:  # computador escolher PEDRA
            print('EMPATE')
        elif computador == 1:  # computador escolher PAPEL
            print('O COMPUTADOR GANHOU !!!!!')
        elif computador == 2:  # computador escolher TESOURA
            print('O JOGADOR GANHOU !!!!!')

    elif jogador == 1:  # jogador escolher PAPEL
        if computador == 0:  # computador escolher PEDRA
            print('O jogador GANHOU !!!!!')
        elif computador == 1:  # computador escolher PAPEL
            print('EMPATE')
        elif computador == 2:  # computador escolher TESOURA
            print('O computador GANHOU !!!!')

    elif jogador == 2:  # jogador escolher TESOURA
        if computador == 0:  # computador escolher PEDRA
            print('O computador GANHOU !!!!!')
        elif computador == 1:  # computador escolher PAPEL
            print('O jogador GANHOU !!!!!')
        elif computador == 2:  # computador escolher TESOURA
            print('EMPATE')

else:
    print('Opção inválida, tente novamente.')






