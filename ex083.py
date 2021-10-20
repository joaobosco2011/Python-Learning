parenteses_abertos = list ()
parenteses_fechados = list ()
expressao = list()

expressao = str(input('Digite uma expressão matermática: '))

for i in expressao:
    
    if i == '(':
        parenteses_abertos.append(i)
    
    if i == ')':
        parenteses_fechados.append(i)
    
if len(parenteses_abertos) == len(parenteses_fechados):
    print('Sua expressão é válida.')
else:
    print('Sua expressão não é válida.')
