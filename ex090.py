alunos = {}
alunos['nome'] = str(input('Informe o nome do aluno: '))
alunos['media'] = float(input('Informe a média do aluno: '))

if alunos['media'] >= 7:
    alunos['situacao'] = 'APROVADO'
else:
    alunos['situacao'] = 'REPROVADO'

print('-=' * 15)

for k, v in alunos.items():
    print(f'{k} é igual a {v}')
