"""
Objetivo: Resolver questão 3 do segundo laboratorio.
"""
from math import pow, pi, cos
import numpy as np


def cosseno(a):  # calcula o cosseno do angulo
    soma = 0
    for i in range(0, 30):
        soma = soma + (pow(-1, i) * (pow(a, 2 * i) / fatorial(2 * i)))
        # o primeiro elemento escolhe o sinal, o segundo o numero da expressão
    return soma


def fatorial(n):  # calcula o fatorial de um numero qualquer
    if n == 0:
        return 1
    else:
        x = 1
        for i in range(1, n + 1):
            x = x * i
        return x


# usaremos numpy para gerar um lista onde o passo possa ser float, coisa que no for não se pode
c = np.arange(0, pi + 0.00001, (pi / 100))  # +0.00001 para que o valor de pi tambem entre no array

cossenos_aprox = [cosseno(i) for i in c]
# gera uma lista onde cada item é valor de uma iteração do for aplicando a função
print(f'Valores aproximados = {cossenos_aprox}')

cossenos_exatos = [cos(i) for i in c]  # lista com valores exatos dos cossenos
print(f'Valores exatos = {cossenos_exatos}')

erro = abs(cossenos_exatos[-1] - cossenos_aprox[-1])
# como o erro aumenta a cada iteração da nossa função, escolhendo o ultimo valor de cada lista, teremos o maior erro
# possivel
print(f'Erro absoluto = {erro}')
