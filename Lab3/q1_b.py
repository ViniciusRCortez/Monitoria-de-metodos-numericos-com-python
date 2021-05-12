"""
Objetivo: Resolver questão 1b do terceiro laboratorio.
    é exatamente o mesmo codigo da questão anterior porém mudando a função a ser passada e o palpite
"""
import matplotlib.pyplot as plt
from math import cos, sin, pi
import numpy as np
from Newton_Raphson import newton_raphson

y = lambda x: cos(x) - x  # f(x) = cos(x) - x, recebendo valores em radianos
y_linha = lambda x: -sin(x) - 1  # f'(x) = -sen(x) - 1, recebendo valores em radianos
ini = 0.5  # ponto inicial
#Verificar o arquivo Nexton-Raphson.py para entender o funcionamento dessa função
resp = newton_raphson(ini, y, y_linha)
print(f'Para essa situação levamos {resp["iterações"] - 1} iterações e temos como valor de f(x) = {resp["modulo"]}')
print('Abaixo seguem os graficos dos valores de f(x) e dos erros, respectivamente:')

# Grafico com os valores de f(x)
x_a = np.linspace(0.4, 0.8, 30)  # valores escolhidos para melhor visualização do grafico
y_a = [y(i) for i in x_a]
plt.style.use('ggplot')
plt.figure(figsize=(7, 5))
plt.title('F(x) por X')
plt.xlabel('Valores de x')
plt.ylabel('Valores de f(x)')
# função com valores entre 0.4 e 0.8
plt.plot(x_a, y_a, label='Função exata')
# Nossa aproximação Newton-Raphson por iteração
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
