"""
Questão 2 do laboratorio 7: Interpolação por MMQ pela seria de Fourier(exponencial)
"""
import numpy as np
from math import pi, sin
import matplotlib.pyplot as plt


def sistemaAumentado(x, y, dim):
    m = len(x)
    A = np.empty((dim, dim))
    b = np.empty((dim))
    soma = []
    for i in range(0, dim + 2):
        aux = 0
        for k in range(0, m):
            aux = aux + x[k] ** i
        soma.append(aux)

    for i in range(0, dim):
        for j in range(i, dim):
            A[i, j] = soma[i + j]
            if (i != j):
                A[j, i] = A[i, j]

    b = []
    for i in range(0, dim):
        aux = 0
        for k in range(0, m):
            aux = aux + y[k] * (x[k] ** (i))
        b.append(aux)

    return A, b


T = 2*pi
Im = 1
x = np.linspace(-T/2, T/2, 30)
y = np.array([])
for i in x:
    if (-T/2) <= i < 0:
        y = np.append(y, 0)
    else:
        y = np.append(y, Im*sin((2*pi/T)*i))
n_x = np.arange(x[0], x[-1], 0.001)
A, b = sistemaAumentado(x, y, 3)
aprox = np.linalg.solve(A, b)
aprox = aprox[::-1]
p = np.poly1d(aprox)
plt.plot(x, y, 'ro', label='Pontos marcados')
plt.plot(n_x, p(n_x), 'r-', label='MMQ')
plt.title('MMQ')
plt.xlabel('X')
plt.ylabel('Y')
plt.style.use('ggplot')
plt.tight_layout()
plt.legend(loc='best')
plt.grid()
plt.show()
