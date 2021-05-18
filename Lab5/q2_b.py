"""
Objetivo: Resolver questão 2b do quinto laboratorio.
"""
import numpy as np
from Funcao_q2 import FuncQ2  # ver arquivo Funcao_q2
from time import time_ns

# USANDO NEWTON-RAPHSON MODIFICADO:
t_inicial = time_ns()
x_1 = [5.0]  # listas com os valores encontrados de x
x_2 = [5.0]
x_3 = [5.0]
func = FuncQ2(x_1[-1], x_2[-1], x_3[-1])
#No metodo mdificado, calculamos o jacobiano somente uma vez
jacobiano = np.array([[func.da_x(), func.da_y(), func.da_z()], #derivadas da eq_1 aplicada ao primeiro (x1,x2,x3)
                      [func.db_x(), func.db_y(), func.db_z()], #derivadas da eq_2 aplicada ao primeiro (x1,x2,x3)
                      [func.dc_x(), func.dc_y(), func.dc_z()]]) #derivadas da eq_3 aplicada ao primeiro (x1,x2,x3)
while True:
    func = FuncQ2(x_1[-1], x_2[-1], x_3[-1])
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
t_final = time_ns()
print(f'Pelo método de Newton-Raphson modificado as três funções se cruzam no ponto:\n({x_1[-1]}, {x_2[-1]}, {x_3[-1]})')
print(f'Levando {(t_final - t_inicial)*(10**-9)} segundos')

#PELO METODO DE QUASENEWTON DE BROYDEN:
t_inicial = time_ns()
x_1 = [5.0]  # Reinicia as listas
x_2 = [5.0]
x_3 = [5.0]
func = FuncQ2(x_1[-1], x_2[-1], x_3[-1])
#Depois da primeira iteração vamos substituir o jacobiano por outra coisa
jacobiano = np.array([[func.da_x(), func.da_y(), func.da_z()],
                      [func.db_x(), func.db_y(), func.db_z()],
                      [func.dc_x(), func.dc_y(), func.dc_z()]])
while True:
    func = FuncQ2(x_1[-1], x_2[-1], x_3[-1])
    funcoes = np.array([[-func.a()],      #eq_1 aplicada ao ultimo (x1,x2,x3)
                        [-func.b()],      #eq_2 aplicada ao ultimo (x1,x2,x3)
                        [-func.c()]])     #eq_3 aplicada ao ultimo (x1,x2,x3)

    solucao = np.linalg.solve(jacobiano, funcoes)   #resolve o sistema matricial
    x_1.append(x_1[-1] + float(solucao[0]))  # atualiza valores de x_1, x_2, x_3
    x_2.append(x_2[-1] + float(solucao[1]))
    x_3.append(x_3[-1] + float(solucao[2]))
    erro_x1 = abs(x_1[-1] - x_1[-2])  # erro absoluto de x_1
    erro_x2 = abs(x_2[-1] - x_2[-2])  # erro absoluto de x_2
    erro_x3 = abs(x_3[-1] - x_3[-2])  # erro absoluto de x_3
    if erro_x1 < 10**(-6) and erro_x2 < 10**(-6) and erro_x3 < 10**(-6):
        break
    func_n = FuncQ2(x_1[-1], x_2[-1], x_3[-1])
    funcoes_novas = np.array([[func_n.a()],      #F(x_n+1)
                        [func_n.b()],
                        [func_n.c()]])
    y = funcoes_novas + funcoes #F(x_n+1) - F(x_n)
    y -= funcoes                #Lembrando que J.s = -F, ou seja, a variavel funcoes j[a esta negativa
    numerador = np.dot(y, np.transpose(solucao))
    denominador = np.dot(np.transpose(solucao), solucao)
    ajuste_jacobiano = numerador/denominador    #incremento da formula de Broyden
    jacobiano += ajuste_jacobiano               #jacobiano ajustado
t_final = time_ns()
print(f'Pelo método de Quase-Newton de Broyden as três funções se cruzam no ponto:\n({x_1[-1]}, {x_2[-1]}, {x_3[-1]})')
print(f'Levando {(t_final - t_inicial)*(10**-9)} segundos')
