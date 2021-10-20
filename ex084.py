nome = ''
peso = ''
cadastro = list()
resposta = ''
tot_pessoas = 0
maior = 0
menor = 0

while resposta != 'n':
    nome = str(input('Informe o nome: '))
    peso = float(input('Informe o peso: '))
    cadastro.append(nome)
    cadastro.append(peso)
    resposta = str(input('Deseja continuar [S/N]? ')).strip().lower()[0]
    tot_pessoas = tot_pessoas + 1

print(f'Ao todo foram cadastradas {tot_pessoas} pessoas.') 

for i in range(1, len(cadastro), 2):
    if i == 1:
        menor = cadastro[i]
    
    if cadastro[i] > maior:
        maior = cadastro[i]

    if cadastro[i] < menor:
        menor = cadastro[i]

print(f'O maior peso foi {maior:.1f} e pertence a ', end=' ')
for c in range(1, len(cadastro), 2):
    if cadastro[c] == maior:
        print(cadastro[c - 1], end= ", ")

print(f'\nO menor peso foi {menor} e pertence a ', end=' ')
for d in range(1, len(cadastro), 2):
    if cadastro[d] == menor:
        print(cadastro[d - 1], end=', ')
