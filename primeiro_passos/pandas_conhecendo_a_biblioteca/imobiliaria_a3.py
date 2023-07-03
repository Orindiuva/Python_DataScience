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


