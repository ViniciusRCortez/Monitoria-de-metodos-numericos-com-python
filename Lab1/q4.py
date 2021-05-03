"""
Objetivo: Resolver questão 4 do primeiro laboratorio.
"""
import numpy as np
from math import pi


def conta(y):       #Realiza cada operação para o valor de y recebido
    a = (-1) ** y
    b = 1 / ((2 * y) + 1)
    return a * b


itens = [100, 1000, 5000]       #Os valores de n para cada um dos itens do enunciado
for item in itens:              #Repete o processo para cada item
    print(f'\nPara n = {item}')
    v_1 = np.arange(item+1)     #Cria um vetor que começa em 0 e termina em n
    v_2 = np.array([])          #Cria um vetor vazio
    for i in v_1:               #Repete para cada valor de v_1 ate n
        x = conta(i)            #Recebe o valor da expressão para o i atual
        v_2 = np.insert(v_2, v_2.size, x)   #adiciona o valor de x no fim do vetor v_2
    soma = v_2.sum()
    erro = abs((pi/4) - soma)
    print(f'Valor do vetor do indice v_1 = \n{v_1}')
    print(f'Valor do vetor da operação v_2 = \n{v_2}\n')
    print(f'Valor do somatorio de v_2 = {soma}')
    print(f'Valor do erro absoluto = {erro}')
