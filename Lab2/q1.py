"""
Objetivo: Resolver questão 1 do segundo laboratorio.
"""

from math import exp
import matplotlib.pyplot as plt
import numpy as np


def f(n):   #Calcula o valor de um I passado
    e = exp(1)
    I = (1 / e) * (e - 1)   #I0
    soma = 0
    for c in range(0, n + 1):   #Calcula cada I ate In de maneira sucessiva
        if c == 0:
            I_n = I
        else:
            I_n = 1 - (1 / (c + 1)) * soma
        soma = I_n
    # ao final temos In = soma
    return soma


x = np.arange(0, 301, 1)    #Gera array de 0 a 300
y = [f(i) for i in x]       #Gera lista de f(0) a f(300)

#Layout do grafico
plt.style.use('ggplot')
plt.figure(figsize=(7, 5))
plt.xlabel('Valores de n')
plt.ylabel('Valores de I')
#Gera o grafico
plt.plot(x, y)
plt.tight_layout()
#Plota o grafico
plt.show()
