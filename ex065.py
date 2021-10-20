n = 0
opcao = ''
soma = 0
cont = 0
media = 0
maior = 0
menor = 0
while opcao != 'n':
    n = int(input('Digite um número inteiro: '))
    opcao = str(input('Você deseja continuar [S/N]? ')).strip().lower()[0]
    soma = soma + n
    cont = cont + 1
    if n > maior:
        maior = n
    if cont == 1:
        menor = n
    if n < menor:
        menor = n
media = soma / cont
print(f'Você digitou {cont} número(s) e a média é {media}.')
print(f'O maior valor foi {maior} e o menor foi {menor}.')


