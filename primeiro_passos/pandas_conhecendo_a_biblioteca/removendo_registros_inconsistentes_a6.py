"""
Alguns registros existentes na base de dados não fazem muito sentido, por exemplo:

apartamentos que possuem valor de aluguel igual a 0;
apartamentos com o valor do condomínio igual a 0.
Esses registros são inconsistentes, por isso devemos removê-los da nossa base de dados.

"""

import pandas as pd

imoveis_comerciais = ['Conjunto Comercial/Sala',
                      'Prédio Inteiro', 'Loja/Salão',
                      'Galpão/Depósito/Armazém',
                      'Casa Comercial', 'Terreno Padrão',
                      'Loja Shopping/ Ct Comercial',
                      'Box/Garagem', 'Chácara',
                      'Loteamento/Condomínio', 'Sítio',
                      'Pousada/Chalé', 'Hotel', 'Indústria']

df = pd.read_csv('dados_aluguel.csv', sep=";")
df = df.query('@imoveis_comerciais not in Tipo and Tipo == "Apartamento"')
df = df.fillna(0)

#Pedando os index dos registro a serem deletados.
df = df.query('Valor == 0 | Condominio == 0').index
print(df)

#Reover apartamentes e Condominío com valor igual a zero

