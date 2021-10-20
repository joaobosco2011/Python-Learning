primeiro_termo = int(input('Informe o primeiro termo da PA: '))
razao = int(input('Informe a razão da PA: '))
pa = 0
for i in range(1, 10):
    if i == 1:
        pa = primeiro_termo
    else:
        pa = pa + razao
    print(pa, end=' ')
if razao > 0:
    print('Essa PA é crescente.')
elif razao == 0:
    print('Essa PA é constante.')
else:
    print('Essa PA é decrescente.')


