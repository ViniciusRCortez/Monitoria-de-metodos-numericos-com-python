"""
Objetivo: Resolver questão 2 do quarto laboratorio.
"""

from Funcoes import LU, Gauss_Siedel
import numpy as np

A = np.array([[1.19, 2.11, -100, 1],
              [14.2, -0.122, 12.2, -1],
              [0, 100, -99.9, 1],
              [15.3, 0.11, -13.1, -1]], dtype='float16')
P = np.array([[1.12],
              [3.44],
              [2.15],
              [4.16]], dtype='float16')

#Por LU:
s = LU(A, P)
print(f'O vetor solução pelo metodo da decomposição LU é: \n{s}')
#Por Gauss-Siedel
s = Gauss_Siedel(A, P, 10)
print(f'O vetor solução pelo metodo da Gauss-Siedel é: \n{s}')
print('Como vemos, o valor deu muito distante em comparação com o outro metodo, isso ocorre porque para essa matriz',
      ' o metodo não converge.')
