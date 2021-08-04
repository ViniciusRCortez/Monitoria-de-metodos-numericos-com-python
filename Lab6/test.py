from Metodos_numericos.metodos import *
import numpy as np
import pandas as pd
a = {"algo":1,
     "dnv":2}

db = pd.DataFrame(a, index=['Erro absoluto'], columns=['algo', 'dnv'])
print(db)
