n = 0
cont = 0
soma = 0
while True:
    n = int(input('Digite um valor [999 para parar]: '))
    if n == 999:
        break
    cont = cont + 1
    soma = soma + n
print(f'A soma do(s) {cont} valor(es) é {soma}.')


