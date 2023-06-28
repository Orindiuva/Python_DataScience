
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

""""
Charlie está trabalhando com uma base de dados de clientes de uma loja.

As quatro primeiras colunas representam dados pessoais dos clientes e ele não pode usá-las na análise. 
Por isso, ele pretende construir um novo array de nome intencao_compras para armazenar apenas as duas últimas 
colunas dos dados. Qual comando ele deve utilizar para o resultado desejado?
"""
clientes = np.array([[1, 'João', 30, 'Rua A', 100, 'eletrônicos'],
                     [2, 'Maria', 25, 'Rua B', 200, 'moda'],
                     [3, 'Pedro', 35, 'Rua C', 50, 'esportes']])

intencao_compra = clientes[:, 4:6]
print(intencao_compra)



"""
Thaís queria desenhar um círculo com a ajuda do computador. Para desenhar a parte superior do círculo ela sabia que deveria usar a equação:

y = sqrt(1 - x ^ 2)

E para a parte inferior bastava utilizar a mesma equação multiplicada por -1.

Qual sequência de código ela deve usar para construir o gráfico corretamente usando a Numpy e sabendo que ambas as partes do círculo devem ter a mesma cor?
"""



# Gerar uma sequência de valores de x de -1 a 1
x = np.arange(-1, 1, 0.0001)
#print(x)
# Implementação da fórmula
y1 = np.sqrt(1 - x**2)
#print(y1)
y2 = -np.sqrt(1 - x**2)

# Plotar o gráfico com as duas partes do círculo
plt.plot(x, y1, 'r')
plt.plot(x, y2, 'r' )

# Adicionar o título do gráfico e os rótulos dos eixos x e y
plt.title("Círculo")
plt.xlabel("Eixo x")
plt.ylabel("Eixo y")

# Exibir o gráfico
#plt.show()


"""
Márcia queria gerar duas sequências de números aleatórios diferentes entre 0 e 5 dentro do seu código. Considere que ela escreveu o seguinte:
A sequência de código vai gerar 5 números entre 0 e 1. Além disso, o seed(42) vai fazer com que as duas sequências sejam iguais.
"""

import numpy as np

np.random.seed(42)
a = np.random.uniform(0, 1, 5)
np.random.seed(42)
b = np.random.uniform(0, 1, 5)
print("xxxxxxxxxxxxxxxxxxxxxxxxxxx")
print(a, b)


"""
Você começou os seus estudos com a biblioteca Numpy e resolveu utilizá-la para substituir um cálculo que estava sendo 
realizado com listas do Python. A lista que você tem em mãos é igual a:
"""
x = [0,1,2,3,4,5,6,7,8,9,10]

"""
Essa lista estava sendo utilizada para calcular os diversos valores de y na equação y = x + 3 / 2. Como ficaria o código em Numpy para substituir o seguinte trecho de código?
"""
print("xxxxxxxxxxxxxxxxxxxxxxxxxxx")
x = [0,1,2,3,4,5,6,7,8,9,10]
y = []

for i in x:
  y.append(i + 3 / 2)

print(y)

x = np.array([0,1,2,3,4,5,6,7,8,9,10])
print(x + 3/2)