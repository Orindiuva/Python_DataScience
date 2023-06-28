"""
Situação: Recebemos a demanda de transformar uma lista com o nome e as notas dos três trimestres de estudantes em uma
          lista simples com os nomes separados das notas e uma lista de listas com as três notas de cada estudante separadas umas das outras.
          Os dados recebidos correspondem a uma lista com os nomes e as respectivas notas de cada estudante.
          Vamos resolver esse desafio? Para facilitar o nosso entendimento do processo vamos trabalhar com uma turma fictícia de 5 estudantes.
"""

notas_turma = ['João', 8.0, 9.0, 10.0, 'Maria', 9.0, 7.0, 6.0, 'José', 3.4, 7.0, 7.0, 'Cláudia', 5.5, 6.6, 8.0, 'Ana', 6.0, 10.0, 9.5]

nomes=[]
notas_juntas=[]
for index, nota in enumerate(notas_turma):
    if(index % 4 == 0):
        nomes.append(nota)
    else:
        notas_juntas.append(nota)
print(nomes)
print(notas_juntas)

print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
notas =[]
for i in range(0, len(notas_juntas), 3):
    notas.append([notas_juntas[i], notas_juntas[i+1], notas_juntas[i+2]])
print(notas)

dicionario = {}
for i,v in enumerate(nomes):
    dicionario[v] = notas[i]


