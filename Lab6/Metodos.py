"""
Implementação dos metodos de interpolação de Newton e de Lagrange.
"""
import numpy as np


def Pol_Newton(x, y, po, pf):
    """
    Implementação do metodo de interpolação de Newton.
    :param x: Vetor com os valores de X.
    :param y: Vetor com os valores de Y.
    :param po: O valor inicial de X onde se pretende calcular a aproximação.
    :param pf: O valor final de X onde se pretende calcular a aproximação.
    :return: Dicionario com os valores entre os ponto pedidos e suas respectivas aproximações de F(x).
    """
    tam = len(x)
    res = np.array([], dtype='float32')
    pontos = np.linspace(po, pf, 100)       #Intervalo a ser calculado
    for p in pontos:
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
        res = np.append(res, pol)
    resultado = {"X": pontos,
                 "Y": res}
    return resultado


def Pol_Lagrange(x, y, po, pf):
    """
    Implementação do metodo de interpolação de Lagrande.
    :param x: Vetor com os valores de X.
    :param y: Vetor com os valores de Y.
    :param po: O valor inicial de X onde se pretende calcular a aproximação.
    :param pf: O valor final de X onde se pretende calcular a aproximação.
    :return: Dicionario com os valores entre os ponto pedidos e suas respectivas aproximações de F(x).
    """
    res = np.array([], dtype='float32')
    r = 0
    tam = len(x)
    pontos = np.linspace(po, pf, 100)  # Intervalo a ser calculado
    for ponto in pontos:
        for i in range(0, tam):         #Cada ordem de y(i)L(i)
            produtorio = 1              #L(i)
            for j in range(0, tam):
                if j != i:
                    produtorio *= (ponto - x[j])/(x[i] - x[j])
            r += produtorio*y[i]
        res = np.append(res, r)
        r = 0
    resultado = {"X": pontos,
                 "Y": res}
    return resultado
