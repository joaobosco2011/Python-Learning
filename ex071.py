saque = int(input('Qual valor você deseja sacar? R$ '))
cont_cedulas_50 = 0
cont_cedulas_20 = 0
cont_cedulas_10 = 0
cont_cedulas_5 = 0
cont_cedulas_1 = 0
saldo = 0
if (saque // 50) > 0:  # função para contar as notas de R$ 50,00
    cont_cedulas_50 = saque // 50
    saldo = saque - (cont_cedulas_50 * 50)
    print(f'Total de {cont_cedulas_50} cédulas de R$ 50,00.')
if (saldo // 20) > 0:  # função para contar as notas de R$ 20,00
    cont_cedulas_20 = saldo // 20
    saldo = saldo - (cont_cedulas_20 * 20)
    print(f'Total de {cont_cedulas_20} cédulas de R$ 20,00.')
if (saldo // 10) > 0:  # função para contar as notas de R$ 10,00
    cont_cedulas_10 = saldo // 10
    saldo = saldo - (cont_cedulas_10 * 10)
    print(f'Total de {cont_cedulas_10} cédulas de R$ 10,00.')
if (saldo // 5) > 0:  # função para contar as notas de R$ 5,00
    cont_cedulas_5 = saldo // 5
    saldo = saldo - (cont_cedulas_5 * 5)
    print(f'Total de {cont_cedulas_5} cédulas de R$ 5,00.')
if (saldo // 1) > 0:  # função para contar as notas de R$ 1,00
    cont_cedulas_1 = saldo // 1
    saldo = saldo - (cont_cedulas_1 * 1)
    print(f'Total de {cont_cedulas_1} cédulas de R$ 1,00.')

