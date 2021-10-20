cadastro = dict()
from datetime import date
ano_nascimento = 0
idade = 0
ano_atual = date.today().year
carteira_trabalho = 0

cadastro['nome'] = str(input('Nome: '))
ano_nascimento = int(input('Ano de nascimento: '))
idade = ano_atual - ano_nascimento
cadastro['idade'] = idade
carteira_trabalho = int(input('Carteira de trabalho (0 não tem): '))
cadastro['ctps'] = carteira_trabalho
if carteira_trabalho == 0:
    for k, v in cadastro.items():
        print(f' - {k} tem o valor de {v}')
else:
    cadastro['ano de contratação'] = int(input('Ano de contratação: '))
    cadastro['salario'] = float(input('Salário: '))
    cadastro['aposentadoria'] = 65 - idade
    for k, v in cadastro.items():
        print(f' - {k} tem o valor de {v}')
