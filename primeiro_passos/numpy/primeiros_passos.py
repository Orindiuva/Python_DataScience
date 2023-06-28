import numpy as np

#np.loadtxt("apples_ts.csv", delimiter=",")

""""
Ao executarmos, é retornado um erro, informando que não foi possível converter uma string em um float. Isso acontece porque, 
quando trabalhamos com arrays em NumPy, precisamos que exista somente um único tipo de dado dentro do array.

Nossa intenção é trabalhar somente com valores numéricos. Mas note que, na primeira coluna, temos textos correspondentes aos 
nomes das cidades. Sendo assim, precisamos solicitar todas as colunas, com exceção desta, de índice zero

Para este array, usaremos a função np.arange() que deve gerar a sequência de valores.

Adicionaremos esta função em uma nova célula.

Nela passamos os índices das colunas, iniciando por 1. Em nosso dataset, temos 7 anos de informação e cada ano possui 12 meses,
 então 7x12 = 84; adicionamos + 3 (correspondente aos 3 meses de 2020) e obtivemos 87. Sendo assim, nossa lista vai de 1 a 87.

Porém, no Python, precisamos digitar o valor final +1 para que este último dado seja englobado, ou seja, 88. Por fim, precisamos passar o valor de incremento, que é 1:
"""

lista = range(1, 88, 1)
dataset = np.loadtxt("apples_ts.csv", delimiter=",", usecols=lista)

"""
ndim: verifica a quantidade de dimensões do array. Ao executarmos o comando a seguir:
Obtemos 2 como retorno. Este valor refere-se à quantidade de informações pelas quais nossos dados estão variando. 
Em nosso caso, temos um dado tabelado 2D, 2 dimensões, linhas e colunas
"""
print("Dimessões do dataset {}".format(dataset.ndim))

#Outra informação que podemos obter é a quantidade de elementos de um array
print("Tamanho do dataset {}".format(dataset.size))

#shape para verificar o número de elementos em cada dimensão:
print(f"Número de linhas {dataset.shape[0]}. Número de colunas {dataset.shape[1]}.")

"""
Mas, como já dito, podemos inverter a estrutura dos nossos dados trocando as linhas por colunas. Para isso, utilizamos o método da transposição, T:
"""
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
dataset = dataset.T
print(dataset)
"""
Situação:
Dado o exemplo de evento periódico acima, crie um array, utilizando a função np.arange(), que liste todos os 
anos onde aconteceram ou estão previstos de acontecer a Copa do Mundo, considerando o intervalo fechado dos anos de 2000 a 2102.
Dica: A primeira Copa do Mundo aconteceu no ano de 2002.
"""
ano_inicial = 2002
ano_final = 2025
copas = range(ano_inicial, ano_final, 4)

"""
A função np.arange(), assim como a função range() do Python considera o intervalo aberto à direita, seguindo o padrão [inicio, fim).
Então, se precisamos avaliar o número ao fim do intervalo, devemos considerar uma unidade a mais (2103): também acontece uma Copa do Mundo no ano de 2102, mas desta maneira, ela não é considerada no array

copas = range(ano_inicial, ano_final+1, 4)


ex = range(1, 10)
for i in ex:
    print(i)

print('xxxxxxxxxxxxxxxxxxxxxxxxxx')
ex = range(1, 10+1)
for i in ex:
    print(i)
"""

print("xxxxxxxxxxxxx - Exercicio - xxxxxxxxxxxxxxxxxxxxxxxxx")
url = 'https://raw.githubusercontent.com/allanspadini/numpy/dados/bytebank.csv'
import numpy as np
dado= np.loadtxt(url, delimiter=',',skiprows=1,dtype=float)
print(dado)
print(dado.shape)