"""
Resolução das questões do Lab6.
"""
import matplotlib.pyplot as plt
from Metodos_numericos.metodos import *

x = np.arange(0, 5.1, 1, dtype='float16')    #Pontos de X
f = lambda c: c**2                      #F(x)
y = np.array([], dtype='float16')       #Pontos de Y
pol = np.array([], dtype='float16')     #Pontos da aproximação
for i in x:
    y = np.append(y, f(i))
#Para o Metodo de Newton:
pol = interpol(x, y, 0, 5)
pol.Newton()
plt.plot(pol.resultado["X"], pol.resultado["Y"], 'r-', label='Valores aproximados')
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
pol = interpol(x, y, 0, 5)
pol.Lagrange()
plt.plot(pol.resultado["X"], pol.resultado["Y"], 'r-', label='Valores aproximados')
plt.plot(x, y, 'bx', label='Valores medidos')
plt.xlabel("Valores de X")
plt.ylabel('Valores de F(x)')
plt.title('Grafico de interpolação de Lagrange')
plt.style.use('ggplot')
plt.tight_layout()
plt.legend(loc='best')
plt.show()
