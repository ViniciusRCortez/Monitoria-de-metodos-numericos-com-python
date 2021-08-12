"""
Terceira questão do Lab8: Integração numerica.
"""
from Metodos_numericos.metodos import Integral
from math import exp

#QUESTÃO 1:
f = lambda x: exp(-x)*x**2
a = 0
b = 1
n = 4
I = Integral(f, a, b, n)
I.Trapezio()
print(f'Para o metodo do Trapezio com {n} subdivisões recebemos o valor de I = {I.resultado:.4f}')
I.Simpson()
print(f'Para o metodo do Simpson com {n} subdivisões recebemos o valor de I = {I.resultado:.4f}')
