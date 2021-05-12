"""
Objetivo: Resolver questão 1b do terceiro laboratorio.
    é exatamente o mesmo codigo da questão anterior porém mudando a função a ser passada e o palpite
"""
import matplotlib.pyplot as plt
from math import cos, sin, pi
import numpy as np


def newton_raphson(n, f, f_linha):
    x = [n]  # x(n), sendo inicialmente nosso palpite
    erro = []
    func = [f(x[-1])]
    while True:
        # a cada iteração vamos adicionar um novo valor de x à lista
        # x[-1] é o ultimo elemento de uma lista
        x.append(x[-1] - f(x[-1]) / f_linha(x[-1]))  # x(n+1) pela formula de Newton-Raphson
        func.append(f(x[-1]))
        erro.append(abs(x[-1] - x[-2]))  # erro absoluto
        if erro[-1] < 10 ** (-6):
            break
    resultado = {
        'modulo': abs(f(x[-1])),  # ultimo valor do f(x)
        'iterações': len(x),  # numero de iterações, tamonho da lista-1 pois a lista inicia com nosso palpite
        'erros': erro,  # uma lista com os diferentes valores de erro
        'valores': x,  # uma lista com os diferentes valores de x
        'valores_função': func  # uma lista com os diferentes valores de f(x)
    }
    return resultado


y = lambda x: cos(x) - x  # f(x) = cos(x) - x, recebendo valores em radianos
y_linha = lambda x: -sin(x) - 1  # f'(x) = -sen(x) - 1, recebendo valores em radianos
ini = 0.5  # ponto inicial
resp = newton_raphson(ini, y, y_linha)
print(f'Para essa situação levamos {resp["iterações"] - 1} iterações e temos como valor de f(x) = {resp["modulo"]}')
print('Abaixo seguem os graficos dos valores de f(x) e dos erros, respectivamente:')

# Grafico com os valores de f(x)
x_a = np.linspace(0.4, 0.8, 30)    #valores escolhidos para melhor visualização do grafico
y_a = [y(i) for i in x_a]
plt.style.use('ggplot')
plt.figure(figsize=(7, 5))
plt.title('F(x) por X')
plt.xlabel('Valores de x')
plt.ylabel('Valores de f(x)')
#função com valores entre 0.4 e 0.8
plt.plot(x_a, y_a, label='Função exata')
#Nossa aproximação Newton-Raphson por iteração
plt.plot(resp['valores'], resp['valores_função'], label='Valores de Newton-Raphson por iteração')
plt.tight_layout()
plt.legend(loc='best')
plt.show()
# Grafico com os valores dos erros
plt.style.use('ggplot')
plt.figure(figsize=(7, 5))
plt.title('Erro por Iterações')
plt.xlabel('Numero de iterações')
plt.ylabel('Valores dos erros')
plt.plot([i for i in range(1, resp['iterações'])], resp['erros'])
plt.tight_layout()
plt.show()
