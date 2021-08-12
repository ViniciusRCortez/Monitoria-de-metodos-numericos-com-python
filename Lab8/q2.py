"""
Segunda questão do Lab8: Integração numerica.
"""
from Metodos_numericos.metodos import Integral
from math import cos, pi

#QUESTÃO 1:
f = lambda x: x*cos(x)
a = 0
b = pi/2
n = 2
I = Integral(f, a, b, n)
I.Trapezio()
print(f'Para o metodo do Trapezio com {n} subdivisões recebemos o valor de I = {I.resultado:.4f}')
I.Simpson()
print(f'Para o metodo do Simpson com {n} subdivisões recebemos o valor de I = {I.resultado:.4f}')
n = 4
I = Integral(f, a, b, n)
I.Trapezio()
print(f'Para o metodo do Trapezio com {n} subdivisões recebemos o valor de I = {I.resultado:.4f}')
I.Simpson()
print(f'Para o metodo do Simpson com {n} subdivisões recebemos o valor de I = {I.resultado:.4f}')
