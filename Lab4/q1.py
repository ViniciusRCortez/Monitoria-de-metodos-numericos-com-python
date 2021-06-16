"""
Objetivo: Resolver questão 1 do quarto laboratorio.
"""

from Funcoes import LU, Gauss_Siedel
import numpy as np

A = np.array([[1, 1, -1],
              [1, 1, 4],
              [2, -1, 2]], dtype='float16')
P = np.array([[1],
              [2],
              [3]], dtype='float16')

#Por LU:
s = LU(A, P)
print(f'O vetor solução pelo metodo da decomposição LU é: \n{s}')
#Por Gauss-Siedel
s = Gauss_Siedel(A, P, 10)
print(f'O vetor solução pelo metodo da Gauss-Siedel é: \n{s}')
print('Como vemos, o valor deu muito distante em comparação com o outro metodo, isso ocorre porque para essa matriz',
      ' o metodo não converge.')
