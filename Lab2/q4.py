"""
Objetivo: Resolver questão 4 do segundo laboratorio.
"""
from math import pow, pi


def conta(a):
    soma = 0
    for i in range(0, a + 1):
        numerador = 4 * pow(-1, i)
        denominador = (2 * i) + 1
        x = numerador / denominador
        soma = soma + x
    return soma


# item a
n = 0
while True:
    y = conta(n)
    erro_abs = abs(pi - y)
    if erro_abs < 0.0001:
        break   #sai do loop ao encontrar o pirmeiro valor desejado
    n += 1
print(f'Erro absoluto = {erro_abs}\nValor encontrado = {y}')

#item b
n = 0
while True:
    y = conta(n)
    erro_rel = abs(pi - y)
    erro_rel = erro_rel/pi
    if erro_rel < 0.001:    #0.001 = 0.1%
        break
    n += 1
print(f'\nErro relativo = {erro_rel*100}%\nValor encontrado = {y}')

# item c
n = 0
while True:
    y = conta(n)
    erro_aprx = abs(pi - y)
    if round(erro_aprx, 5) < 0.0001:
        #round(numero, casas_decimais) aproxima um numero para o numero de casas decimais especificados(deafult=0)
        break
    n += 1
print(f'\nErro aproximado = {round(erro_aprx, 5)}\nValor encontrado = {y}')

#item d
n = 0
while True:
    y = conta(n)
    erro_aprx_rel = abs(pi - y)
    erro_aprx_rel = erro_aprx_rel/pi
    if round(erro_aprx_rel, 4) < 0.001:
        break
    n += 1
print(f'\nErro aproximado relativo = {round(erro_aprx_rel, 4)*100}%\nValor encontrado = {y}')
