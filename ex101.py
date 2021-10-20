from datetime import date

ano_atual = date.today().year

def voto(ano):
    idade = ano_atual - ano

    if idade <16: ## define quem é menor de 16 anos e não vota
        print( f'Com {idade} anos: NÂO VOTA')

    if 16 <= idade < 18: ## define quem tem voto opcional com idade entre 16 e 18 anos
        print( f'Com {idade} anos: VOTO OPCIONAL')

    if 18 <= idade < 70: ## define quem é maior de idade e tem voto obrigatório
        print( f'Com {idade} anos: VOTO OBRIGATÓRIO')
    else:
        print( f'Com {idade} anos: VOTO OPCIONAL')


## PROGRAMA PRINCIPAL
print('-' * 27)
voto(int(input('Em que ano você nasceu? ')))
