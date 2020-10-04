def calcula_f(x):
    return x**3 + 5 * x ** 2 - 5 * x - 12

iteracao_maxima = 100
iteracao = 0 
erro_definido = 0.0001
parar = 0

a = -6.0
b = -4.0

y1 = calcula_f(a)
y2 = calcula_f(b)

c_anterior =  2 * b

if y1 * y2 > 0:
    print('erro de execucao - redefinir valores de a e b')
else:
    while parar == 0:
        print('no loop')
        iteracao = iteracao + 1
        c = b - (y2 * (b - a))/(y2 - y1)

        yc = calcula_f(c)

        if y2 * yc > 0:
            b = c 
        
        erro = abs(c - c_anterior)
        c_anterior = c

        if (iteracao > iteracao_maxima) or (erro > erro_definido):
            parar = 1

print('\ntotal de iteração', iteracao)
print('\nvalor de x = ', c)
print('\nErro encontrado, erro = ', erro, '\n')