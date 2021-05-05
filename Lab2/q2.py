"""
Objetivo: Resolver questão 2 do segundo laboratorio.
"""


def fibonachi(n):
    if n == 1 or n == 0:
        return 0    #primeiro elemento é 0
    elif n == 2:
        return 1    #segundo elemento é 1
    else:
        f_anterior = 0
        f_atual = 1
        f_aux = 0
        for c in range(0, n - 2):       #(n-2) para compensar o fato da serie iniciar com 0 e 1
            f_aux = f_atual
            f_atual = f_atual + f_anterior
            f_anterior = f_aux
        return f_atual  #terceiro ou mais elemento é calculado


resultado = fibonachi(9)
print(resultado)
