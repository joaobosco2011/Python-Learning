n = int(input('Informe o primeiro termo da PA: '))  # primeiro termo da PA
r = int(input('Informe a razão da PA: '))  # razão da PA
pa = 0  # variável que irá acumular a soma da PA
i = 0
opcao = 1  # variável para mais iterações da PA
cont = 10  # contador de iterações da PA
for c in range(1, 11):  # soma dos 10 primeiros termos da PA
    if c == 1:
        pa = n
    else:
        pa = pa + r
    print(pa)
while opcao != 0:  # soma de mais "n" termos da PA
    opcao = int(input('Quantos termos você quer mostrar a mais? '))
    for i in range (0, opcao):
        pa = pa + r
        print(pa)
        cont = cont + 1
print(f'Progressão finalizada com {cont} termos mostrados.')







