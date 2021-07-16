from Metodos_numericos.metodos import *

f = lambda x: x**2
p0 = 0.5
a = raizes(f)
a.ponto_fixo(p0)
print(a.x)

