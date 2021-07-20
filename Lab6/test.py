from Metodos_numericos.metodos import *
import numpy as np

y = lambda x: x**3 - 9*x + 5
d = lambda x: 3*x**2 - 9
p = lambda x: (5 + x**3)/9
x = raizes(y, 0.5)
x.bissecao(0.5, 1)
print(f'para bicesseção: {x.x}')

x.posicao_falsa(0.5, 1)
print(f'para pfalsa: {x.x}')

x.ponto_fixo(p)
print(f'para pfixo: {x.x}')

x.secante(1, 2)
print(f'para sec: {x.x}')

x.secante_mod(0.01)
print(f'para secm: {x.x}')

x.Newton_Raphson(d)
print(f'para nr: {x.x}')


