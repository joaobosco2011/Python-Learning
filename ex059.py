divisao = 0
multiplicacao = 0
subtrair = 0
soma = 0
p_numero = int(input('Informe o primeiro número: '))
s_numero = int(input('Informe o segundo número: '))
opcao = int(input('-------------------------\n'
                  'Escolha uma opçao abaixo:\n'
                  '[1] somar\n'
                  '[2] subtrair\n'
                  '[3] multiplicar\n'
                  '[4] dividir\n'
                  '[5] maior número\n'
                  '[6] menor número\n'
                  '[7] digitar novos números\n'
                  '[0] ENCERRAR O PROGRAMA\n'
                  'Qual o número da sua opção? '))
while not opcao == 0:
    if opcao == 1:  # funçao de soma
        soma = p_numero + s_numero
        print(f'A soma entre {p_numero} + {s_numero} = {soma}')
        opcao = int(input('-------------------------\n'
                          'Escolha uma opçao abaixo:\n'
                          '[1] somar\n'
                          '[2] subtrair\n'
                          '[3] multiplicar\n'
                          '[4] dividir\n'
                          '[5] maior número\n'
                          '[6] menor número\n'
                          '[7] digitar novos números\n'
                          '[0] ENCERRAR O PROGRAMA\n'
                          'Qual o número da sua opção? '))
    elif opcao == 2:  # função de subtração
        subtrair = p_numero - s_numero
        print(f'A subtração entre {p_numero} - {s_numero} = {subtrair}')
        opcao = int(input('-------------------------\n'
                          'Escolha uma opçao abaixo:\n'
                          '[1] somar\n'
                          '[2] subtrair\n'
                          '[3] multiplicar\n'
                          '[4] dividir\n'
                          '[5] maior número\n'
                          '[6] menor número\n'
                          '[7] digitar novos números\n'
                          '[0] ENCERRAR O PROGRAMA\n'
                          'Qual o número da sua opção? '))
    elif opcao == 3:  # funçao de multiplicação
        multiplicacao = p_numero * s_numero
        print(f'A multiplicação entre {p_numero} x {s_numero} = {multiplicacao}')
        opcao = int(input('-------------------------\n'
                          'Escolha uma opçao abaixo:\n'
                          '[1] somar\n'
                          '[2] subtrair\n'
                          '[3] multiplicar\n'
                          '[4] dividir\n'
                          '[5] maior número\n'
                          '[6] menor número\n'
                          '[7] digitar novos números\n'
                          '[0] ENCERRAR O PROGRAMA\n'
                          'Qual o número da sua opção? '))
    elif opcao == 4:  # função de divisão
        divisao = p_numero / s_numero
        print(f'A divisão entre {p_numero} ÷ {s_numero} = {divisao}')
        opcao = int(input('-------------------------\n'
                          'Escolha uma opçao abaixo:\n'
                          '[1] somar\n'
                          '[2] subtrair\n'
                          '[3] multiplicar\n'
                          '[4] dividir\n'
                          '[5] maior número\n'
                          '[6] menor número\n'
                          '[7] digitar novos números\n'
                          '[0] ENCERRAR O PROGRAMA\n'
                          'Qual o número da sua opção? '))
    elif opcao == 5:  # função para mostrar o maior número
        if p_numero > s_numero:
            print(f'O maior número entre {p_numero} e {s_numero} é {p_numero}.')
        else:
            print(f'O maior número entre {p_numero} e {s_numero} é {s_numero}.')
        opcao = int(input('-------------------------\n'
                          'Escolha uma opçao abaixo:\n'
                          '[1] somar\n'
                          '[2] subtrair\n'
                          '[3] multiplicar\n'
                          '[4] dividir\n'
                          '[5] maior número\n'
                          '[6] menor número\n'
                          '[7] digitar novos números\n'
                          '[0] ENCERRAR O PROGRAMA\n'
                          'Qual o número da sua opção? '))
    elif opcao == 6:  # função para mostrar o menor número
        if p_numero < s_numero:
            print(f'O menor número entre {p_numero} e {s_numero} é {p_numero}.')
        else:
            print(f'O menor número entre {p_numero} e {s_numero} é {s_numero}.')
        opcao = int(input('-------------------------\n'
                          'Escolha uma opçao abaixo:\n'
                          '[1] somar\n'
                          '[2] subtrair\n'
                          '[3] multiplicar\n'
                          '[4] dividir\n'
                          '[5] maior número\n'
                          '[6] menor número\n'
                          '[7] digitar novos números\n'
                          '[0] ENCERRAR O PROGRAMA\n'
                          'Qual o número da sua opção? '))
    elif opcao == 7:  # função para novos números
        p_numero = int(input('Informe o primeiro número: '))
        s_numero = int(input('Informe o segundo número: '))
        opcao = int(input('-------------------------\n'
                          'Escolha uma opçao abaixo:\n'
                          '[1] somar\n'
                          '[2] subtrair\n'
                          '[3] multiplicar\n'
                          '[4] dividir\n'
                          '[5] maior número\n'
                          '[6] menor número\n'
                          '[7] digitar novos números\n'
                          '[0] ENCERRAR O PROGRAMA\n'
                          'Qual o número da sua opção? '))
    else:  # caso o usuário digite uma opção inválida
        print('Opção inválida, tente novamente com as disponíveis abaixo.')
        opcao = int(input('-------------------------\n'
                          'Escolha uma opçao abaixo:\n'
                          '[1] somar\n'
                          '[2] subtrair\n'
                          '[3] multiplicar\n'
                          '[4] dividir\n'
                          '[5] maior número\n'
                          '[6] menor número\n'
                          '[7] digitar novos números\n'
                          '[0] ENCERRAR O PROGRAMA\n'
                          'Qual o número da sua opção? '))
print('Fim do programa.')





