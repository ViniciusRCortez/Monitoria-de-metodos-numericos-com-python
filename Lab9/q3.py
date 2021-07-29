"""
Questão 3 do laboratorio 9: Interpolação por MMQ à determinar.
"""
import numpy as np
import matplotlib.pyplot as plt
from Metodos_numericos.metodos import interpol

x = np.arange(0, 15, 1)
y = np.array([0, 0.292, 0.387, 0.752, 0.921, 1.0, 0.961, 1.01, 1.07, 1.14, 1.011, 1.036, 1.093, 1.181, 1.219])

print('A partir de analise grafica verificamos q a utilização de um polinomio de grau 8 descreve bem o conjunto de dados'
      ' como o mostrado a seguir:')
pol = interpol(x, y, x[0], x[-1])
pol.MMQ(8)
plt.plot(x, y, 'yo', label='Dados medidos')
plt.plot(pol.resultado["X"], pol.resultado["Y"], 'g-', label='Interpolação')
plt.title('MMQ Parabolico')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend(loc='best')
plt.style.use('ggplot')
plt.tight_layout()
plt.grid()
plt.show()

aprox = pol.resultado["X"].tolist()
for i in range(0, len(aprox)):
    aprox[i] = round(aprox[i], 1)
index = aprox.index(2.7)
print('O valor de y(2.71)=', round(pol.resultado["Y"][index], 3))
