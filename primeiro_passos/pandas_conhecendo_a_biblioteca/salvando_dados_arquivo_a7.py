import pandas as pd

imoveis_comerciais = ['Conjunto Comercial/Sala',
                      'Prédio Inteiro', 'Loja/Salão',
                      'Galpão/Depósito/Armazém',
                      'Casa Comercial', 'Terreno Padrão',
                      'Loja Shopping/ Ct Comercial',
                      'Box/Garagem', 'Chácara',
                      'Loteamento/Condomínio', 'Sítio',
                      'Pousada/Chalé', 'Hotel', 'Indústria']

df = pd.read_csv('dados_aluguel.csv', sep=';')

df = df.query('@imoveis_comerciais not in Tipo')
df = df.query('Tipo == "Apartamento"')
df.fillna(0)
index_delecao = df.query('Valor == 0 | Condominio == 0').index
df.drop(index_delecao, axis=0, inplace=True)
df.drop(columns='Tipo', axis=1, inplace=True)
print(df.head(5))

df.to_csv('dados_apartamento.csv', sep=';')

"""
O retorno é um dataframe completo, com algo diferente dos anteriores: a coluna "Unnamed: 0". 
Quando salvamos um arquivo em formato CSV, ele automaticamente gera novos índices ordenados para cada uma das nossas linhas 
e os índices antigos do nosso dataframe vão para outra coluna: a "Unnamed: 0". Ela não tem nenhuma utilidad
"""

df_apartamento = pd.read_csv('dados_apartamento.csv', sep=';')
print(df_apartamento.head(5))

"""
Para salvarmos os nossos dados sem essa coluna, podemos adicionar um parâmetro no momento do salvamento. 
Então, copiaremos a linha de código do to_csv() e, colaremos na próxima célula e, após o nome do arquivo, 
adicionaremos vírgula, seguida do parâmetro index=False.
"""
df.to_csv('dados_apartamento.csv', sep=';', index=False)
df_apartamento = pd.read_csv('dados_apartamento.csv', sep=';')
print(df_apartamento.head(5))

