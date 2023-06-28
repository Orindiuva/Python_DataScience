import numpy as np

"""
Chegamos ao coeficiente angular através da geração de números aleatórios. Mas a intenção é que você, na sua máquina,

consiga gerar os mesmos números aleatórios gerados na máquina do instrutor.

Quando utilizamos uma geração de números aleatórios, não estamos fazendo isso efetivamente.

Se executarmos o seguinte comando diversas vezes, obteremos diferentes resultados:

"""

print(np.random.uniform(low=0.10,high=0.90,size=100))

"""
Ainda assim, não são números totalmente aleatórios, pois partem de um cálculo que parte de uma semente,
então se utilizarmos a mesma semente conseguiremos gerar a mesma sequência de números aleatórios.

Esta semente é um número definido que será utilizado para uma sequência de cálculos da função geradora de números 
aleatórios da NumPy. Utilizando o mesmo número conseguiremos gerar a mesma sequência.
"""
print()
np.random.seed(16)
print(np.random.uniform(low=0.10,high=0.90,size=100))