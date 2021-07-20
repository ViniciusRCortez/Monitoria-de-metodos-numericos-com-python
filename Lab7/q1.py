"""
Questão 1 do laboratorio 7: Interpolação por spline quadratica.
"""
import numpy as np
import matplotlib.pyplot as plt
from Metodos_numericos.metodos import *

x = np.array([-3.142, -2.513, -1.885, -1.257, - 0.628, 0.000, 0.628, 1.257, 1.885, 2.513, 3.142])
fx = np.array([-0.032, -0.039, -0.091, 1.091, 1.039, 1.032, 1.039, 1.091, -0.091, -0.039, -0.032])

#Para o spline quadratico
pol = interpol(x, fx, x, fx)
pol.Spline(tipo=2)
tam = pol.resultado["Y"].shape[1]           #Quantidade de seguimentos do spline
plt.plot(pol.resultado["X"], pol.resultado["Y"], 'r-')
plt.plot(x, fx, 'bx')
plt.xlabel("Valores de X")
plt.ylabel('Valores de F(x)')
plt.title('Grafico de Spline quadratico')
plt.style.use('ggplot')
plt.tight_layout()
plt.grid()
plt.show()
