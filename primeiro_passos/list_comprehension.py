"""
A List comprehension é uma forma simples e concisa de criar listas, sendo que essas listas seguirão alguns padrões, via condicionais, laços e outras expressões.
O formato padrão é: [exressão for item in lista]

Entre colchetes, temos uma expressão. Ela está em um item que está dentro da lista. Essa lista poderia ser um iterável, como uma tupla ou os valores de um dicionário.
A ideia é pegar cada elemento desse iterável e aplicar uma expressão. É bem parecido com lambda, mas, neste caso, estamos trabalhando com a geração de uma lista.

"""


lista_idade= [15, 20, 14, 17, 30, 99, 74, 12, 2, 23]
lista_maior_idade = [idade for idade in lista_idade if idade > 18]
print(lista_maior_idade)


"""
Recebemos a demanda de criar uma lista com as médias dos estudantes da lista de listas que criamos na Situação 6. 
Lembrando que cada lista da lista de listas possui as três notas de cada estudante.
"""

notas = [[8.0, 9.0, 10.0], [9.0, 7.0, 6.0], [3.4, 7.0, 7.0], [5.5, 6.6, 8.0], [6.0, 10.0, 9.5]]

media = [round(sum(nota)/len(nota), 2) for nota in notas]
print("Medias das nota : {}".format(media))


def media(lista: list=[0]) -> float:
    calculo = sum(lista) / len(lista)
    return calculo

media = [round(media(nota),2) for nota in notas]
print("Medias das nota : {}".format(media))

"""
Agora, precisamos utilizar as médias calculadas no exemplo anterior, pareando com o nome dos estudantes. 
Isto será necessário para gerar uma lista que selecione aqueles estudantes que possuam uma média final maior ou igual a 8 para concorrer a uma bolsa para o próximo ano letivo.

Os dados recebidos correspondem a uma lista de tuplas com os nomes e códigos dos estudantes e a lista de médias calculadas logo acima.

Vamos resolver esse desafio?

Para facilitar o nosso entendimento do processo vamos trabalhar com uma turma fictícia de 5 estudantes.
"""
print("xxxxxxxxxxxxxxxxxxxxx ---- xxxxxxxxxxxxxxxxxxxxxxxxxxx")
nomes = [('João', 'J720'), ('Maria', 'M205'), ('José', 'J371'), ('Cláudia', 'C546'), ('Ana', 'A347')]
medias = [9.0, 7.3, 5.8, 6.7, 8.5]


lista_nomes = [nome[0] for nome in nomes]
print(lista_nomes)
nova_lista = zip(lista_nomes, medias)
print(type(nova_lista))
print("elegiveis")
nova_lista = list(nova_lista)
print(nova_lista)
print(nova_lista[0])
alunos_elegiveis = [aluno[0] for aluno in nova_lista if aluno[1] >= 8.0]

print(alunos_elegiveis)


#################################
"""
A zip() é uma função embutida do Python que recebe um ou mais iteráveis (lista, string, dict, etc.) e retorna-os como 
um iterador de tuplas onde cada elemento dos iteráveis são pareados. Ela é útil para fazer iterações simultâneas em várias listas.
"""
print("xxxxx - zip - xxxxxxx")
lista1 = [1, 2, 3,4,5]
lista2 = [1.1, 2.2, 3.3, 4.4, 5.5]

nova_lista = zip(lista1, lista2)
print(list(nova_lista))

id = [1, 2, 3, 4, 5]
regiao = ["Norte", "Nordeste", "Sudeste", "Centro-Oeste", "Sul"]

mapa = list(zip(id, regiao))
print(mapa)


id = [1, 2, 3, 4, 5]
regiao = ["Norte", "Nordeste", "Sudeste"]

mapa = list(zip(id, regiao))
print(mapa)
print("----------xxxx x------")
"""
Para fazer o processo contrário, de transformar uma tupla iterável em listas, basta passar o operador asterisco (*) 
ao lado esquerdo do nome da tupla iterável que quer extrair os dados, repassando cada tupla para uma variável.
"""

tupla_iteravel = [('J392', 'João'), ('M890', 'Maria'), ('J681', 'José'), ('C325', 'Claúdia'), ('A49', 'Ana')]
ids, nomes  = zip(*tupla_iteravel)

ids = list(ids)
nomes = list(nomes)

print("IDs = ", ids)
print("Nomes = ", nomes)