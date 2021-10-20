sum_idade = 0
media = 0
maior = 0
velho = ''
cont_20 = 0
for c in range (1, 5):
    print(f'----- {c}ª PESSOA -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (M/F): ')).upper()
    sum_idade = sum_idade + idade
    if sexo == 'M' and idade > maior:
        maior = idade
        velho = nome
    elif sexo == 'F' and idade < 20:
        cont_20 = cont_20 + 1
media = sum_idade / 4
print(f'A média  de idade do grupo é de {media} anos.')
print(f'O homem mais velho tem {maior} anos e se chama {velho}.')
print(f'Ao todo são {cont_20} mulher(es) com menos de 20 anos.')

