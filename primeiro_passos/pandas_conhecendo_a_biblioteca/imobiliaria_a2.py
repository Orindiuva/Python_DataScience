import pandas as pd
import numpy as np
desired_width = 320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', None) # coluna
pd.set_option('display.max_rows', None) # linha

#np.set_printoptions(suppress=True)
pd.options.display.float_format = '{:.2f}'.format
dados = pd.read_csv("dados_aluguel.csv", delimiter=";")
print(dados.head(n=5))
print()
print("Número de linhas: {} - Número de colunas: {}".format(dados.shape[0], dados.shape[1]))
print()
print(dados.describe())
print()
print("Colunas do dataset:{}".format(dados.columns))
print()
print(dados.info())
print()
#Aqui é retornando uma series que contém o index + valor
print("Tipo de imóvei: {}".format(dados['Tipo'].head(5)))
print('-- Imóveis presentes no dataset')
print("Tipo de imóvei: {}".format(dados['Tipo'].unique()))

print("-----------------")
print(dados[['Quartos', 'Valor']].head(5))

"""
O processo de Análise Exploratória de Dados (EDA) consiste em buscar entender como são estruturados os dados que queremos analisar.

É um processo de caráter investigativo, onde tentamos compreender várias características, como: os valores presentes nas colunas, os tipos de estrutura de dados, verificar se são dados qualitativos ou quantitativos, se há valores faltantes ou incomuns.

Por isso, nesse momento, perguntas sobre os dados são sempre bem-vindas. Elas irão guiar todo o processo de análise, e, através das ferramentas disponíveis, como o nosso querido Pandas, iremos buscar por respostas.

Algumas perguntas que podemos fazer nesse momento:

Quais os valores médios de aluguel por tipo de imóvel?
Qual o percentual de cada tipo de imóvel na nossa base de dados?
"""

