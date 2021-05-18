"""
Objetivo: Resolver questão 1 do quinto laboratorio.
"""
from math import exp
import numpy as np

x = [1.5]  # listas com os valores encontrados de x
y = [0]  # listas com os valores encontrados de y
diodo = lambda x, y: 0.6*exp(x/25) - y
reta = lambda x, y: 100 - (200/3)*x - y

#Derivadas parciais do diodo:
diodo_x = lambda x, y: 0.6*x*exp(x/25)
diodo_y = lambda x, y: -1
#Derivadas parciais da reta:
reta_x = lambda x, y: -200/3
reta_y = lambda x, y: -1

while True:
    #matrizes:
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

print(f'As duas funções se cruzam no ponto ({x[-1]}, {y[-1]})')
