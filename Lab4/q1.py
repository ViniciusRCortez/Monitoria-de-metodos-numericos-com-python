"""
Objetivo: Resolver questão 1 do quarto laboratorio.
"""

from Funcoes import LU
import numpy as np

#Por LU:
A = np.array([[1, 1, -1],
              [1, 1, 4],
              [2, -1, 2]], dtype='float16')
P = np.array([[1],
              [2],
              [3]], dtype='float16')
s = LU(A, P)
print(f'O vetor solução é: \n{s}')
