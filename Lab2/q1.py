"""
Objetivo: Resolver questão 1 do segundo laboratorio.
"""
import sympy
from math import exp


def conta(a):
    e = exp(1)  # exponencial de 1
    if a <= 0:
        I = (1 / e) * (e - 1)  # I0
        return I
    else:
        I_novo = 1 - (1 / (a + 1)) * conta(a - 1)  # Recursiva para tratar o I(n+1)
        return I_novo


n = sympy.Symbol('n')
# n = float()
l = sympy.limit(conta(n), n, 0)
f = 1 / n
g = sympy.limit(f, n, 0)
# sympy.plot(conta(n), xlim=[-10, 10], ylim=[-10, 10])
print(g)
