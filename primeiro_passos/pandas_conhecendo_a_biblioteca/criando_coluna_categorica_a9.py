"""
O time de desenvolvimento solicitou a criação de mais duas colunas. No entanto, dessa vez elas são categóricas:

Descrição: essa coluna deve possuir uma sumarização das principais informações dos imóveis que serão apresentadas no site: tipo de imóvel, bairro, quantidade de quartos e vagas de garagem;
Possui_suite: essa deve ser uma coluna que informe apenas se o imóvel possui ou não suítes, sem se importar com a quantidade.

"""


import pandas as pd

df = pd.read_csv('dados_aluguel.csv', sep=';')
df['Descricao'] = df.
