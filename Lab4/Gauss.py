
import numpy as np


a = np.array([[3, 0.841, -0.841],
              [2, -1250, 0],
              [-2.71, -2.71, 20]])   #gera um array aleatorio(com numeros float e negativos
b = np.array([[1.951],
              [-624.25],
              [-7.809]])

#função pro metodo de gauss:
a = a.astype('float')   #transforma a matriz em float, pois como int daria erro de arredondamento
b = b.astype('float')
##elinação:
###garantir pivos n nulos:
tam = np.size(a, 0) #Numero de elementos na coluna 0
len = len(a[0][:])
print(f'{a}\n{b}')
for i in range(tam):    #busca pivos = 0 e soma alguma linha com eles
    if a[i][i] == 0:
        for c in range(tam):    #encontra uma linha cujo elemento na coluna do pivo[i][i] != 0
            if a[c][i] != 0:
                a[i][:] = a[i][:] + a[c][:]
                b[i][:] = b[i][:] + b[c][:]
                break
###Eliminar td abaixo da diagonal principal mantendo as correlações
for k in range(len):    #coluna a ser operada
    for i in range(k + 1, tam):  # linha a ser corrigida
        base_a = a[k][:]    #linha anterior
        base_b = b[k][:]
        if a[i][k] != 0:
            m = a[i][k]/base_a[k]   #numero para multiplicar e zerar o elemento abaixo
            a[i][:] = a[i][:] - m*base_a    #opera a linha
            b[i][:] = b[i][:] - m * base_b  #opera a linha
print(f'{a}\n{b}')
