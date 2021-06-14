from scipy.linalg import lu_factor, lu_solve


def LU(A, P):
    """
    Resolve o sistema pelo metodo LU.
    :param A: Matriz dos coeficientes.
    :param P: Matriz dos valores independentes.
    :return: Matriz da solução.
    """
    lu, piv = lu_factor(A)
    solucao = lu_solve((lu, piv), P)
    return solucao

