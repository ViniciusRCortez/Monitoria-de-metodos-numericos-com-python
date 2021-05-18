"""
Objetivo: Resolver questão 2a do quinto laboratorio.
"""
from math import exp, cos, pi, sin
import numpy as np

#USANDO NEWTON-RAPHSON
x_1 = [1.0]  # listas com os valores encontrados de x
x_2 = [1.0]
x_3 = [-1.0]
const = ((10*pi)-3)/3   #constante
a = lambda x_1, x_2, x_3: 3*x_1 - cos(x_2*x_3) - 0.5
b = lambda x_1, x_2, x_3: x_1**2 - 625*x_2**2 - 0.25
c = lambda x_1, x_2, x_3: exp(-x_1*x_2) + 20*x_3 + const

#Derivadas parciais de eq_1:
dax_1 = lambda x_1, x_2, x_3: 3
dax_2 = lambda x_1, x_2, x_3: -sin(x_2*x_3)*x_3
dax_3 = lambda x_1, x_2, x_3: -sin(x_2*x_3)*x_2

#Derivadas parciais de eq_2:
dbx_1 = lambda x_1, x_2, x_3: 2*x_1
dbx_2 = lambda x_1, x_2, x_3: -625*2*x_2
dbx_3 = lambda x_1, x_2, x_3: 0

#Derivadas parciais de eq_1:
dcx_1 = lambda x_1, x_2, x_3: exp(-x_1*x_2)*(-x_2)
dcx_2 = lambda x_1, x_2, x_3: exp(-x_1*x_2)*(-x_1)
dcx_3 = lambda x_1, x_2, x_3: 20

"""while True:
    #matrizes
    jacobiano = np.array([[reta_x(x[-1], y[-1]), reta_y(x[-1], y[-1])], #derivadas da reta aplicada ao ultimo (x,y)
                          [diodo_x(x[-1], y[-1]), diodo_y(x[-1], y[-1])]])#derivadas do diodo aplicada ao ultimo (x,y)
    funcoes = np.array([[-reta(x[-1], y[-1])],      #equação da reta aplicada ao ultimo (x,y)
                        [-diodo(x[-1], y[-1])]])    #equação do diodo aplicada ao ultimo (x,y)

    solucao = np.linalg.solve(jacobiano, funcoes)   #resolve o sistema matricial

    x.append(x[-1] + float(solucao[0]))             #atualiza valores de x e y
    y.append(y[-1] + float(solucao[1]))
    erro_x = abs(x[-1] - x[-2])     #erro absoluto de x
    erro_y = abs(y[-1] - y[-2])     #erro absoluto de y
    if erro_x < 10**(-6) and erro_y < 10**(-6):
        break

print(f'As duas funções se cruzam no ponto ({x[-1]}, {y[-1]})')"""
