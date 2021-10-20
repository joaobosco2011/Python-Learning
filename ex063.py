print('-----Sequência de Fibonacci-----')
i = int(input('Quantos termos você quer mostrar? '))
fn = 0
fn1 = 1
fn2 = 0
t = 0
for i in range(1, i+1):
    fn = fn1 + fn2
    print(fn)
    t = fn1
    fn1 = fn
    fn2 = t

