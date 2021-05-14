"""
Objetivo: Resolver questão 2a do terceiro laboratorio.
    é exatamente o mesmo codigo da questão anterior porém mudando a função a ser passada e o palpite
"""
import matplotlib.pyplot as plt
import numpy as np
from Newton_Raphson import newton_raphson

#PARA X0 = 1
y = lambda x: 180*x**3 - 117*x**2 - 80*x + 52  # f(x) = 180x^3 - 117x^2 - 80x + 52
y_linha = lambda x: 540*x**2 - 234*x - 80  # f'(x) = 540x^2 - 234x - 80
ini = 1  # ponto inicial
#Verificar o arquivo Nexton-Raphson.py para entender o funcionamento dessa função
resp = newton_raphson(ini, y, y_linha, 'q2')
print(f'Para essa X0 = 1 levamos {resp["iterações"] - 1} iterações e temos como valor de f(x) = {resp["modulo"]}')
print('Abaixo seguem os graficos dos valores de f(x) e dos erros, respectivamente:')

# Grafico com os valores de f(x)
x_a = np.linspace(-1.2, 1.2, 30)  # valores escolhidos para melhor visualização do grafico
y_a = [y(i) for i in x_a]
plt.style.use('ggplot')
plt.figure(figsize=(7, 5))
plt.title(f'F(x) por X\ncom X0 = 1')
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

#PARA X0 = -1
y = lambda x: 180*x**3 - 117*x**2 - 80*x + 52  # f(x) = 180x^3 - 117x^2 - 80x + 52
y_linha = lambda x: 540*x**2 - 234*x - 80  # f'(x) = 540x^2 - 234x - 80
ini = -1  # ponto inicial
#Verificar o arquivo Nexton-Raphson.py para entender o funcionamento dessa função
resp = newton_raphson(ini, y, y_linha, 'q2')
print(f'Para essa X0 = -1 levamos {resp["iterações"] - 1} iterações e temos como valor de f(x) = {resp["modulo"]}')
print('Abaixo seguem os graficos dos valores de f(x) e dos erros, respectivamente:')

# Grafico com os valores de f(x)
x_a = np.linspace(-1.2, 1.2, 30)  # valores escolhidos para melhor visualização do grafico
y_a = [y(i) for i in x_a]
plt.style.use('ggplot')
plt.figure(figsize=(7, 5))
plt.title(f'F(x) por X\ncom X0 = -1')
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
