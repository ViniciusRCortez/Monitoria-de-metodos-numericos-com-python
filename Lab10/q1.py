"""
Q1: Resolver as questões do lab 10:
"""
from Metodos_numericos.metodos import EDO
from math import exp
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pprint import pprint

# Declarando constantes:
R = 33000
C = 90*10**(-6)
ti = 0
vi = 1
vo_linha = lambda t, v: -(1/(R*C))*v

#Resultado analitico:
vo = lambda t: exp(-t/(R*C))
x = np.arange(0, 15.01, 0.01)
v_analitico = np.array([vo(i) for i in x])

#Pelo metodo de Euler:
edo = EDO(vo_linha, ti, vi, 0.5)
euler = np.array([])
for i in x:
    edo.Euler(i)
    euler = np.append(euler, edo.y_novo)

#Pelo metodo de Heun:
edo = EDO(vo_linha, ti, vi)
heun = np.array([])
for i in x:
    edo.Heun(i)
    heun = np.append(heun, edo.y_novo)

#Pelo metodo de Runge Kutta 4° ordem:
edo = EDO(vo_linha, ti, vi)
rk = np.array([])
for i in x:
    edo.Runge_Kutta_4(i)
    rk = np.append(rk, edo.y_novo)

#plotando graficos comparativos:
plt.grid()
plt.tight_layout()
plt.style.use('ggplot')
plt.plot(x, v_analitico, 'r-', label='Valor analitico')
plt.plot(x, euler, 'y-', label='Metodo de Euler')
plt.title('Analise de EDO pelo metodo de Euler')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='best')
plt.show()

plt.plot(x, v_analitico, 'r-', label='Valor analitico')
plt.plot(x, heun, 'g-', label='Metodo de Heun')
plt.title('Analise de EDOs pelo metodo de Heun')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='best')
plt.show()

plt.plot(x, v_analitico, 'r-', label='Valor analitico')
plt.plot(x, rk, 'b-', label='Metodo de Runge Kutta de 4º ordem')
plt.title('Analise de EDOs pelo metodo de Runge Kutta')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='best')
plt.show()

#Calculo dos erros:
erro_euler = max(abs(euler - v_analitico))
erro_heun = max(abs(heun - v_analitico))
erro_runge = max(abs(rk - v_analitico))

erros = {
    "Euler": round(erro_euler, 5),
    "Heun": round(erro_heun, 5),
    "Runge Kutta": round(erro_runge, 5)
}
db = pd.DataFrame(erros, index=['Erro absoluto'], columns=['Euler', 'Heun', 'Runge Kutta'])
pprint(db)
