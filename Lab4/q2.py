"""
Objetivo: Resolver questão 2 do quarto laboratorio.
"""

from Funcoes import LU
import numpy as np

#Por LU:
A = np.array([[1.19, 2.11, -100, 1],
              [14.2, -0.122, 12.2, -1],
              [0, 100, -99.9, 1],
              [15.3, 0.11, -13.1, -1]], dtype='float16')
P = np.array([[1.12],
              [3.44],
              [2.15],
              [4.16]], dtype='float16')
s = LU(A, P)
print(f'O vetor solução é: \n{s}')
