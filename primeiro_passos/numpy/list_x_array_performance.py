""""
Existem várias vantagens em usar arrays Numpy ao invés de listas regulares do Python, aqui estão algumas:

Eficiência de processamento
As operações matemáticas em arrays Numpy são muito mais rápidas do que em listas regulares, pois a NumPy foi otimizada para trabalhar com conjuntos de dados homogêneos e libera memória do computador rapidamente.

Facilidade de uso
As operações matemáticas em arrays Numpy são expressas de forma muito mais clara e concisa do que em listas regulares, tornando o código mais fácil de ler e manter.

Integração com outras bibliotecas
A Numpy é uma das bibliotecas mais utilizadas em ciência de dados e aprendizado de máquina, e muitas outras bibliotecas, como a Pandas e a Matplotlib, são projetadas para trabalhar diretamente com arrays Numpy.

Comparativo de performance: listas vs arrays

Focando na eficiência podemos comparar o tempo levado para efetuar um cálculo utilizando listas e arrays.
"""

import numpy as np
import time

# cria uma lista com 1000000 elementos
lista = list(range(1000000))

# transforma a lista em um array Numpy
array = np.array(lista)

# começa a cronometrar o tempo para a operação com a lista
start_time = time.time()

# realiza a operação de elevar ao quadrado cada elemento da lista
lista_quadrado = [i**2 for i in lista]

# para o cronômetro
list_time = time.time() - start_time

# começa a cronometrar o tempo para a operação com o array
start_time = time.time()

# realiza a operação de elevar ao quadrado cada elemento do array
array_quadrado = array**2

# para o cronômetro
array_time = time.time() - start_time

print("Tempo da operação com a lista: ", list_time)
print("Tempo da operação com o array: ", array_time)
