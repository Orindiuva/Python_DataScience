"""
Agora, a nossa demanda consiste em gerar um dicionário a partir da lista de listas que criamos na Situação 10
para passá-la à pessoa responsável por construir as tabelas, possibilitando a análise dos dados.

As chaves do nosso dicionário serão as colunas identificando o tipo de dado.

Os valores serão as listas com os dados correspondentes àquela chave.

"""

lista_completa = [[('João', 'J720'), ('Maria', 'M205'), ('José', 'J371'), ('Cláudia', 'C546'), ('Ana', 'A347')],
                  [[8.0, 9.0, 10.0], [9.0, 7.0, 6.0], [3.4, 7.0, 7.0], [5.5, 6.6, 8.0], [6.0, 10.0, 9.5]],
                  [9.0, 7.3, 5.8, 6.7, 8.5],
                  ['Aprovado', 'Aprovado', 'Reprovado', 'Aprovado', 'Aprovado']]

coluna = ["Notas", "Media Final", "Situacao"]

cadastro = {coluna[i] : lista_completa[i+1] for i in range(len(coluna))}
print(cadastro)

print(' ---- cadastro + estudante ----')
"""
Por fim, vamos adicionar o nome dos estudantes, extraindo apenas seus nomes da lista de tuplas
"""
#cadastro["Estudante"] = [lista_completa[0][i][0] for i in range(len(lista_completa[0]))]
cadastro["Estudante"] = [aluno[0] for aluno in  lista_completa[0]]
print(cadastro)
print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
notas = cadastro['Notas']
medias = cadastro['Media Final']
situacao = cadastro['Situacao']
estudantes = cadastro['Estudante']

cadastro = {}
for index, estudante in enumerate(estudantes):
    cadastro[estudante] = notas[index], medias[index], situacao[index]
print(cadastro)

print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')

cadastro = {}
for index, estudante in enumerate(estudantes):
    cadastro[estudante] = [{"Notas":notas[index]}, {"Media": medias[index]}, {"Situacao": situacao[index]}]
print(cadastro)

print("Lista todos os alunos:")
for key, value in cadastro.items():
    nota = value[0]['Notas']
    media = value[1]['Media']
    situacao = value[2]['Situacao']
    print("Aluno {} obteve as notas {} e média {} sua situação é: {}".format(key,nota,media,situacao))
    print()



print("xxxxxxxxxxxxxxxxxx - Exercicio - #########################")
"""

Recebemos uma demanda da instituição de ensino do nosso projeto. Foi repassado para nós uma lista de 20 estudantes e suas respectivas médias finais. 
Aqui, nós precisamos selecionar estudantes que tenham média final maior ou igual a 9.0. Esses(as) estudantes serão premiados(as) com uma bolsa de estudos para o próximo ano letivo.

Para filtrar os dados, temos que gerar um dicionário cujas chaves são os nomes e os valores são as médias dos(as) estudantes selecionados(as). Estes são os dados recebidos:
"""


nomes_estudantes = [ "Enrico Monteiro", "Luna Pereira", "Anthony Silveira", "Letícia Fernandes",
                    "João Vitor Nascimento", "Maysa Caldeira", "Diana Carvalho", "Mariane da Rosa",
                    "Camila Fernandes", "Levi Alves", "Nicolas da Rocha", "Amanda Novaes",
                    "Laís Moraes", "Letícia Oliveira", "Lucca Novaes", "Lara Cunha",
                    "Beatriz Martins", "João Vitor Azevedo", "Stephany Rosa", "Gustavo Henrique Lima" ]

medias_estudantes = [5.4, 4.1, 9.1, 5.3, 6.9, 3.1, 10.0, 5.0, 8.2, 5.5,
                    8.1, 7.4, 5.0, 3.7, 8.1, 6.2, 6.1, 5.6, 6.7, 8.2]


nomes_medias = list(zip(nomes_estudantes, medias_estudantes))
print(nomes_medias)
dicionario_alunos = {aluno[0]:aluno[1] for aluno in nomes_medias if aluno[1] >=9.0}
print(dicionario_alunos)

dicionario_alunos = {nome:media for nome, media in zip(nomes_estudantes, medias_estudantes) if media >=9.0}
print(dicionario_alunos)