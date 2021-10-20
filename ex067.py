n = 0
while True:
    n = int(input('Digite um número inteiro para ver a sua tabuada [Digite 0 para sair]: '))
    if n == 0:
        break
    else:
        for i in range (1, 11):
            print(f'{i:2} x {n:2} = {n * i}')



