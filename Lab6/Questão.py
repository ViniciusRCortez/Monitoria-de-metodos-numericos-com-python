"""
Resolução das questões do Lab6.
"""
import numpy as np
from Metodos import Pol_Newton
import matplotlib.pyplot as plt

x = np.arange(0, 5, dtype='float16')    #Pontos de X
f = lambda c: c**2                      #F(x)
y = np.array([], dtype='float16')       #Pontos de Y
pol = np.array([], dtype='float16')     #Pontos da aproximação
for i in x:
    y = np.append(y, f(i))

for i in range(len(x)):
    r = Pol_Newton(x, y, i)
    pol = np.append(pol, r)
plt.plot(x, y, 'r-')
plt.plot(x+1, pol, 'g--')
plt.show()
"""CONTINUAR COM A LOGICA PROPOSTA"""
