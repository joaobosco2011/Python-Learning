turma = list()
aluno = list()
nome = ''
nota_1 = ''
nota_2 = ''
resp = ''
media = 0
indice = ''

## leitura e armazenamento do nome e notas dos alunos
while True:
    nome = str(input('Nome do aluno: '))
    aluno.append(nome)
    nota_1 = float(input('Primeira nota: '))
    aluno.append(nota_1)
    nota_2 = float(input('Segunda nota: '))
    aluno.append(nota_2)
    turma.append(aluno[:])
    aluno.clear()
    resp = str(input('Deseja continuar [S/N]? ')).lower().strip()[0]
    if resp in 'nN':
        break

## impressão da lista de alunos com as médias
print('-_' * 20)
print(f'{"Ind.":^3}', f'{"Nome":<10}', f'{"Média":^6}')  # cabeçalho da lista
print('-' * 30)
for i in range(0, len(turma)):  # lista de alunos
    media = (turma[i][1] + turma[i][2]) / 2
    print(f'{i:^3}', f'{turma[i][0]:<10}', f'{media:^6}')

## nota de um aluno específico
while True:
    indice = int(input('Digite o índice para mostrar a nota do aluno (999 para encerrar): '))
    if indice == 999:
        print('Foi um prazer tê-lo aqui!!!')
        break
    else:
        print(f'As notas de {turma[indice][0]} são {turma[indice][1]} e {turma[indice][2]}.')