"""
Questão 2 do laboratorio 9: Interpolação por MMQ Parabolico.
"""
import numpy as np
import matplotlib.pyplot as plt
from Metodos_numericos.metodos import interpol

x = np.array([-2, -1, 1, 3, 4, 4])
y = np.array([4, 2, 1, 3, 5, 6])

pol = interpol(x, y, x[0], x[-1])
pol.MMQ(2)

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
