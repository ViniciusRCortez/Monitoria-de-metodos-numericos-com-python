"""
Objetivo: Resolver questão 3 do primeiro laboratorio.
"""


def conta(a):       #retorna a expressão desejada para cada valor de i
    numerador = ((a ** 3) + 1) ** 2
    denominador = (a ** 2) + 2
    return numerador / denominador


x = [-1.6, -1.2, -0.8, -0.4, 0, 0.4, 0.8, 1.2]
for i in x:     #i = cada valor de x individualmente
    y = conta(i)
    print(f'y = {y}')
