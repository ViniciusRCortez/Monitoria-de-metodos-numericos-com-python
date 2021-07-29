from Metodos_numericos.metodos import *
import numpy as np

def mmq2(x, th, exp, n=0):
    if exp == 0:
        return x * th[n] ** exp
    else:
        return x * th[n] ** exp + mmq(x, th, exp - 1, n + 1)


def mmq(x, th, grau):
    aux = grau
    soma = 0
    for c in range(0, grau):
        soma += th[c]*(x**aux)
        aux -= 1
    soma += th[-1]
    return soma
th = [1, 2, 3, 4]
print(mmq(2, th, 3))


