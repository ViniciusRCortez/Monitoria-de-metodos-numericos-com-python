"""
Objetivo: Resolver questão 5 do primeiro laboratorio.
"""


def ResistenciaEq(Valores_res):
    soma = 0
    for valor in Valores_res:
        soma = soma + (1 / valor)
    soma = 1 / soma
    return soma


n_res = int(input('Numero de resistores: '))        
R = []
for c in range(0, n_res):
    x = float(input(f'Valor do {c + 1}º resistor: '))
    R.append(x)
Req = ResistenciaEq(R)
print(f'Resistência equivalente: {Req}')
