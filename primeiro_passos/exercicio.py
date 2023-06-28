"""
1) Crie um código para imprimir a soma dos elementos de cada uma das listas contidas na seguinte lista:
"""
print("xxxxxxxxxxxxxx --- Exec l --- xxxxxxxxxxxxxxxxxxxx")
lista_de_listas = [[4,6,5,9], [1,0,7,2], [3,4,1,8]]

total = [sum(lista_de_listas[index]) for index in range(len(lista_de_listas))]
print(total, sum(total))

"""
2) Crie um código para gerar uma lista que armazena o terceiro elemento de cada tupla contida na seguinte lista de tuplas:
"""
print("xxxxxxxxxxxxxx --- Exec 2 --- xxxxxxxxxxxxxxxxxxxx")
lista_de_tuplas = [('Pedro', 1.74, 81), ('Júlia', 1.65, 67), ('Otávio', 1.81, 83)]

lista_terceiro_elemento = [elemento[2] for elemento in lista_de_tuplas]
print(lista_terceiro_elemento)

print("xxxxxxxxxxxxxx --- Exec 3 --- xxxxxxxxxxxxxxxxxxxx")
"""
 A partir da lista: lista = ['Pedro', 'Júlia', 'Otávio', 'Eduardo'], crie um código para gerar uma lista de tuplas em
  que cada tupla tenha o primeiro elemento como a posição do nome na lista original e o segundo elemento sendo o próprio nome.
"""

lista = ['Pedro', 'Júlia', 'Otávio', 'Eduardo']
posicao = [posicao[:1] for posicao in lista]
lista_tupla = list(zip(posicao, lista))
print(lista_tupla)

print("xxxxxxxxxxxxxx --- Exec 4 --- xxxxxxxxxxxxxxxxxxxx")
"""
Crie uma lista usando o list comprehension que armazena somente o valor numérico de cada
tupla caso o primeiro elemento seja 'Apartamento', a partir da seguinte lista de tupla
"""

aluguel = [('Apartamento', 1700), ('Apartamento', 1400), ('Casa', 2150), ('Apartamento', 1900), ('Casa', 1100)]

lista = [imovel[1] for imovel in aluguel if imovel[0] == 'Apartamento']
print(lista)

print("xxxxxxxxxxxxxx --- Exec 5 --- xxxxxxxxxxxxxxxxxxxx")
"""
Crie um dicionário usando o dict comprehension em que as chaves estão na lista meses =
 ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'] 
 e os valores estão na lista despesa = [860, 490, 1010, 780, 900, 630, 590, 770, 620, 560, 840, 360].
"""
lista_meses =  ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
lista_despesa = [860, 490, 1010, 780, 900, 630, 590, 770, 620, 560, 840, 360]

dicionario = { mes:despesa for mes, despesa in zip(lista_meses, lista_despesa)}
print(dicionario)

print()
print("xxxxxxxxxxxxxx --- Exec 6 --- xxxxxxxxxxxxxxxxxxxx")
"""
Uma loja possui um banco de dados com a informação de venda de cada representante e de cada ano e precisa filtrar somente 
os dados do ano 2022 com venda maior do que 6000. A loja forneceu uma amostra contendo apenas as colunas com os anos e os 
valores de venda para que você ajude a realizar a filtragem dos dados a partir de um código:
"""

vendas = [('2023', 4093), ('2021', 4320), ('2021', 5959), ('2022', 8883),
          ('2023', 9859), ('2022', 5141), ('2022', 7688),
          ('2022', 9544), ('2023', 4794), ('2021', 7178),
          ('2022', 3030), ('2021', 7471), ('2022', 4226),
          ('2022', 8190), ('2021', 9680), ('2022', 5616)]

report = [venda for venda in vendas if venda[0] == '2022' and venda[1] > 6000]
print(report)

print()
print("xxxxxxxxxxxxxx --- Exec 7 --- xxxxxxxxxxxxxxxxxxxx")
"""
Uma clínica analisa dados de pacientes e armazena o valor numérico da glicose em um banco de dados e gostaria de rotular os dados da seguinte maneira:

 - Glicose igual ou inferior a 70: 'Hipoglicemia'
 - Glicose entre 70 a 99: 'Normal'
 - Glicose entre 100 e 125: 'Alterada'
 - Glicose superior a 125: 'Diabetes'
A clínica disponibilizou parte dos valores e sua tarefa é criar uma lista de tuplas usando list comprehension contendo o rótulo e o valor da glicemia em cada tupla.
"""
glicemia = [129, 82, 60, 97, 101, 65, 62, 167, 87, 53, 58, 92, 66, 120, 109, 62, 86, 96, 103, 88, 155, 52, 89, 73]

rotulo = [ 'Hipoglicemia' if result < 70 else 'Normal' if result >70 and result <=99 else'Alterada' if result >=100 and result < 125 else "Diabetes" for result in glicemia]
report = list(zip(rotulo, glicemia))
print(report)

print()
print("xxxxxxxxxxxxxx --- Exec 8 --- xxxxxxxxxxxxxxxxxxxx")
"""
 Um e-commerce possui as informações de id de venda, quantidade vendida e preço do produto divididos nas seguintes listas:

O e-commerce precisa estruturar esses dados em uma tabela contendo o valor total da venda, que é obtida multiplicando a quantidade 
pelo preço unitário. Além disso, a tabela precisa conter um cabeçalho indicando as colunas: 'id', 'quantidade', 'preco' e 'total'.

Crie uma lista de tuplas em que cada tupla tenha um id, quantidade, preço e valor total, na qual a primeira tupla é o cabeçalho da tabela.

"""

id = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
quantidade = [15, 12, 1, 15, 2, 11, 2, 12, 2, 4]
preco = [93.0, 102.0, 18.0, 41.0, 122.0, 14.0, 71.0, 48.0, 14.0, 144.0]

total = [(quantidade * preco) for quantidade, preco in zip(quantidade, preco) ]
report= (id, quantidade, preco, total)
print(list(zip(id, quantidade, preco, total)))

print()
print("xxxxxxxxxxxxxx --- Exec 9 --- xxxxxxxxxxxxxxxxxxxx")
""""
Uma empresa possui filiais espalhadas nos Estados da região Sudeste do Brasil. Em uma das tabelas de cadastro das filiais 
há uma coluna contendo a informação de qual é o Estado a que pertence: estados = ['SP', 'ES', 'MG', 'MG', 'SP', 'MG', 
'ES', 'ES', 'ES', 'SP', 'SP', 'MG', 'ES', 'SP', 'RJ', 'MG', 'RJ', 'SP', 'MG', 'SP', 'ES', 'SP', 'MG'].

A empresa sempre está abrindo novas filiais, de modo que a tabela está constantemente recebendo novos registros e o 
gestor gostaria de possuir a informação atualizada da quantidade de filiais em cada Estado.

A partir da coluna com a informação dos Estados, crie um dicionário usando dict comprehension com a chave sendo o nome 
de um Estado e o valor sendo a contagem de vezes em que o Estado aparece na lista.

Dica: Você pode fazer um passo intermediário para gerar uma lista de listas em que cada uma das listas 
possui o nome de apenas um Estado com valores repetidos.
"""
estados = ['SP', 'ES', 'MG', 'MG', 'SP', 'MG',
'ES', 'ES', 'ES', 'SP', 'SP', 'MG', 'ES', 'SP', 'RJ', 'MG', 'RJ', 'SP', 'MG', 'SP', 'ES', 'SP', 'MG']

estado_filiais = set(estados)
dicionario_tot_filiais = {}
for estado in estado_filiais:
    dicionario_tot_filiais[estado] = estados.count(estado)
print(dicionario_tot_filiais)

print()
print("xxxxxxxxxxxxxx --- Exec 10 --- xxxxxxxxxxxxxxxxxxxx")

"""
Nessa mesma tabela de cadastro de filiais, há uma coluna com as informações da quantidade de funcionários e o gestor gostaria
de ter um agrupamento da soma de funcionários para cada estado.
A partir da lista de tuplas, crie um dicionário em que as chaves são os nomes dos Estados únicos e os valores são as listas 
com o número de funcionários referentes ao Estado. Crie também um dicionário em que as chaves são os nomes dos 
Estados e os valores são a soma de funcionários por Estado.
 
"""

funcionarios = [('SP', 16), ('ES', 8), ('MG', 9), ('MG', 6), ('SP', 10), ('MG', 4), ('ES',9), ('ES', 7),
                ('ES', 12), ('SP', 7), ('SP', 11), ('MG',8), ('ES',8), ('SP',9), ('RJ', 13), ('MG', 5),
                ('RJ', 9), ('SP', 12), ('MG', 10), ('SP', 7), ('ES', 14), ('SP', 10), ('MG', 12)]

estados = [funcionario[0] for funcionario in funcionarios]
estados = set(estados)
dicionario = {}
for estado in estados:
    dicionario[estado] = [funcionario[1] for funcionario in funcionarios if funcionario[0] == estado]
print(dicionario)

for key, value in dicionario.items():
    dicionario[key] = sum(value)
print(dicionario)