"""
Implementação dos metodos de interpolação de Newton e de Lagrange.
"""
import numpy as np


def Pol_Newton(x, y, p):
    """
    Implementação do metodo de interpolação de Newton.
    :param x: Vetor com os valores de X.
    :param y: Vetor com os valores de Y.
    :param p: O valor de X onde se pretende calcular a aproximação.
    :return: O valor da aproximação de Y.
    """
    #P(x) = d0 + d1(x-x0) + d2(x-x0)(x-x1).....
    tam = len(x)
    FDD = np.ones(tam**2).reshape((tam, tam))*-1#Tabela de diferenças divididas(começa em -1 para visualização)
    for i in range(tam):
        FDD[i][0] = y[i]                        #Primeira coluna
    for i in range(1, tam):
        for j in range(tam-i):                  #Demais colunas
            FDD[j][i] = (FDD[j+1][i-1] - FDD[j][i-1])/(x[j+i] - x[j])    #Faz todas as colunas antes de iterar a linha
    x_termo = 1                                 #Auxiliar para a multiplicaçãos pelos termos de X
    pol = FDD[0][0]                             #Polinomio de Newton
    for ordem in range(1, tam):
        x_termo = x_termo*(p - x[ordem-1])
        pol += FDD[0][ordem]*x_termo            #Operador(primeiro termo de cada coluna)*multiplicação dos x
    return pol

