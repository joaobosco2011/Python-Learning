from datetime import date
ano_atual = date.today().year
idade = 0
maior = 0
menor = 0

for c in range(1, 8, 1):
    ano_nasc = int(input(f'Em que ano a {c}ª pessoa nasceu? '))
    idade = ano_atual - ano_nasc
    if idade >= 18:
        maior = maior + 1
    else:
        menor = menor + 1

print(f'Ao todo tivemos {maior} pessoas maiores de idade.')
print(f'Tivemos {menor} pessoas menores de idade.')
