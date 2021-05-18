"""
Objetivo: Resolver questão 2a do quinto laboratorio.
"""
import numpy as np
from Funcao_q2 import FuncQ2  # ver arquivo Funcao_q2

# USANDO NEWTON-RAPHSON
x_1 = [1.0]  # listas com os valores encontrados de x
x_2 = [1.0]
x_3 = [-1.0]
while True:
    func = FuncQ2(x_1[-1], x_2[-1], x_3[-1])
    #matrizes
    jacobiano = np.array([[func.da_x(), func.da_y(), func.da_z()], #derivadas da eq_1 aplicada ao ultimo (x1,x2,x3)
                          [func.db_x(), func.db_y(), func.db_z()], #derivadas da eq_2 aplicada ao ultimo (x1,x2,x3)
                          [func.dc_x(), func.dc_y(), func.dc_z()]]) #derivadas da eq_3 aplicada ao ultimo (x1,x2,x3)
    funcoes = np.array([[-func.a()],      #eq_1 aplicada ao ultimo (x1,x2,x3)
                        [-func.b()],      #eq_2 aplicada ao ultimo (x1,x2,x3)
                        [-func.c()]])     #eq_3 aplicada ao ultimo (x1,x2,x3)

    solucao = np.linalg.solve(jacobiano, funcoes)   #resolve o sistema matricial

    x_1.append(x_1[-1] + float(solucao[0]))         #atualiza valores de x_1, x_2, x_3
    x_2.append(x_2[-1] + float(solucao[1]))
    x_3.append(x_3[-1] + float(solucao[2]))
    erro_x1 = abs(x_1[-1] - x_1[-2])     #erro absoluto de x_1
    erro_x2 = abs(x_2[-1] - x_2[-2])     #erro absoluto de x_2
    erro_x3 = abs(x_3[-1] - x_3[-2])     #erro absoluto de x_3
    if erro_x1 < 10**(-6) and erro_x2 < 10**(-6) and erro_x3 < 10**(-6):
        break

print(f'Pelo método de Newton-Raphson as três funções se cruzam no ponto:\n({x_1[-1]}, {x_2[-1]}, {x_3[-1]})')
