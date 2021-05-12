
def newton_raphson(n, f, f_linha):
    """
    Função python que encontra a raiz de um polinomio pelo metodo Newton-Raphson
    :param n: Palpite inicial
    :param f: Função a ser usada
    :param f_linha: derivada da função a ser usada
    :return: Dicionario com os elementos pedidos no enunciado da pratica
    """
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
