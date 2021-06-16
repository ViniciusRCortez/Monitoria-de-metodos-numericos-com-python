import numpy as np
from scipy.linalg import lu_factor, lu_solve


def LU(A, P):
    """
    Resolve o sistema pelo metodo LU.
    :param A: Matriz dos coeficientes.
    :param P: Matriz dos valores independentes.
    :return: Matriz da solução.
    """
    lu, piv = lu_factor(A)
    solucao = lu_solve((lu, piv), P)
    return solucao


def Gauss_Siedel(A, P, max_it=1):
    """
    Resolver um sistema pelo metodo de Gauss-Seidel
    :param A: Matriz dos coeficientes
    :param P: Matriz dos valores independentes.
    :param max_it(opcional): O numero de iterações maxima.
    :return: Matriz da solução.
    """
    xn = np.copy(P)*0
    for c in range(0, max_it):  #Repete quantas vezes forem passadas
        for i in range(len(xn)):
            s = P[i].copy()     # s = posição de P
            for j in range(len(xn)):
                if i != j:
                    s -= A[i, j] * xn[j]    #Subtraimos tds A*x exceto onde no x[i]
            s /= A[i, i]                    #Dividimos pelo A em questão
            xn[i] = s                       #Atualizamos vetor resultado
    return xn
