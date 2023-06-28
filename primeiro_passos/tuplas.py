"""
As tuplas são estruturas de dados usadas para armazenar itens em uma única variável. São imutáveis, ou seja, não
permitem adição, alteração ou remoção de seus elementos. Após ser construída, seus dados são fixos.

Situação:
Nesta nova demanda, precisamos gerar uma lista de tuplas com os nomes dos estudantes e o código ID de cada um para a
plataforma de análise dos dados. A criação do código consiste em concatenar a primeira letra do nome do estudante a um
número aleatório de 0 a 999. Os dados recebidos correspondem a uma lista dos nomes de cada estudante.

"""

from random import randint

estudantes = ["João", "Maria", "José", "Cláudia", "Ana"]
estudantes

def gera_identificador():
    return str(randint(a=0, b=999))

lista_identificacao = []

for estudante in estudantes:
    id = estudante[:1] + gera_identificador()
    lista_identificacao.append((estudante,id))

print(lista_identificacao)

teste = ('aa', 'bbb', 'ccc')
print(type(teste))
print(teste[2])