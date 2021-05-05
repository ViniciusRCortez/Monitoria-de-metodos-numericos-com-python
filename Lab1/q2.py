"""
Objetivo: Resolver questão 2, as primeiras duas matirzes primeiro laboratorio.
"""
import numpy as np
from scipy.linalg import toeplitz

a = np.eye(5)       #gera uma matriz identidade do tamanho do parametro
#print(f'Matriz a = \n{a}')
b = np.array([[2, 0, 0, 0, 0],
              [2, 2, 0, 0, 0],
              [2, 2, 2, 0, 0],
              [2, 2, 2, 2, 0],
              [2, 2, 2, 2, 2]])
#print(f'Matriz b = \n{b}')
c = np.diag(np.diag(b))     #extrai a diagonal em questãodiag(matiz, k)
#print(c)
d = np.diagflat([[1, 2], [3, 4]], 1)        #escreve uma matriz onde geral é zero menos a diagonal
                                            # definida nos parametros, q tem q ser escrita de 2 em 2
#print(d)
e = toeplitz([1, 1, 0, 3], [0, 2, 0, 2])    #Escreve uma matriz([d, d-1, d-2, ...], [d(n), d+1, d+2, ...])
#print(e)
b_2 = toeplitz([2, 2, 2, 2, 2], [0, 0, 0, 0, 0])
#print(b_2)
f = np.arange(10, 2, -1)        #gera matriz (começo, fim, passo) mas so uma dimensao
f = f.reshape(2, 4)             #redefine o numero de dimensoes(linha, coluna),se falta ou sobre termo ela n roda
print(f)
