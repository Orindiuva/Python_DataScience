"""
Criar uma lista da situação dos estudantes em que caso sua média seja maior ou igual a 6 receberá o valor "Aprovado" e caso contrário receberá o valor "Reprovado".
Gerar uma lista de listas com:

 - Lista de tuplas com o nome dos estudantes e seus códigos.

 - Lista de listas com as notas de cada estudante.

 - Lista com as médias de cada estudante.

 - Lista da situação dos estudantes de acordo com as médias.

Os dados que utilizaremos são os mesmos que geramos nas situações anteriores (nomes, notas, medias).

"""

nomes = [('João', 'J720'), ('Maria', 'M205'), ('José', 'J371'), ('Cláudia', 'C546'), ('Ana', 'A347')]
notas = [[8.0, 9.0, 10.0], [9.0, 7.0, 6.0], [3.4, 7.0, 7.0], [5.5, 6.6, 8.0], [6.0, 10.0, 9.5]]
#medias = [9.0, 7.3, 5.8, 6.7, 8.5]


lista_nomes = [nome[0] for nome in nomes]
print(lista_nomes)
medias = [round(sum(nota)/len(nota),1) for nota in notas]

medias_estudades = list(zip(lista_nomes, medias))
print(medias_estudades)

print("xxxxxxxxxxxxxx - situação - xxxxxxxxxxxxxxxxx")
situacao = ['aprovado' if aluno[1] >= 6.0 else 'reprovado' for aluno in medias_estudades]
print(list(zip(lista_nomes, situacao)))

print('xxxxxxxxxxxx - cadastro - xxxxxxxxxxxxxxxxxx')
cadastro = [x for x in [nomes, notas, medias, situacao]]
print(cadastro)

"""
Podemos recorrer a uma forma mais simples de gerar uma lista de listas, que usar diretamente as variáveis dentro 
dos colchetes, sem precisar escrever a expressão [expr for item in lista de listas].

Para isso, vamos escrever, entre colchetes, [nomes, notas, medias, situacao]. Passaremos isso para lista_completa
"""
print('xxxxxxxxxxxx - cadastro simplificado - xxxxxxxxxxxxxxxxxx')
cadastro= [nomes,notas, medias, situacao]
print(cadastro)