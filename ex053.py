frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
juntar = ''.join(palavras)
inverso = ''

for l in range (len(juntar) - 1, -1, -1):
    inverso = inverso + juntar[l]

if juntar == inverso:
    print(f'A frase {frase} é um PALÍNDROMO.')
else:
    print(f'A frase {frase} não é um PALÍNDROMO.')
