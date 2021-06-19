"""
Resolução das questões do Lab6.
"""
import numpy as np
from Metodos import Pol_Newton, Pol_Lagrange
import matplotlib.pyplot as plt

x = np.arange(0, 5.1, 1, dtype='float16')    #Pontos de X
f = lambda c: c**2                      #F(x)
y = np.array([], dtype='float16')       #Pontos de Y
pol = np.array([], dtype='float16')     #Pontos da aproximação
for i in x:
    y = np.append(y, f(i))

#Para o Metodo de Newton:
pol = Pol_Newton(x, y, 0, 5)
plt.plot(pol["X"], pol["Y"], 'r-', label='Valores aproximados')
plt.plot(x, y, 'bx', label='Valores medidos')
plt.xlabel("Valores de X")
plt.ylabel('Valores de F(x)')
plt.title('Grafico de interpolação de Newton')
plt.style.use('ggplot')
plt.tight_layout()
plt.legend(loc='best')
plt.grid()
plt.show()

#Para o Metodo de Lagrange:
pol = Pol_Lagrange(x, y, 0, 5)
plt.plot(pol["X"], pol["Y"], 'r-', label='Valores aproximados')
plt.plot(x, y, 'bx', label='Valores medidos')
plt.xlabel("Valores de X")
plt.ylabel('Valores de F(x)')
plt.title('Grafico de interpolação de Lagrange')
plt.style.use('ggplot')
plt.tight_layout()
plt.legend(loc='best')
plt.show()
