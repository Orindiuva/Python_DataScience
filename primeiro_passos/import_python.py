#Para listar todos os pacotes instalados: pip list

#import matplotlib
#Alias
import matplotlib.pyplot as plt
#from nome_biblioteca import metodo para apenas um método de uma dada biblioteca.
#from matplotlib import pyplot
'''
estudantes = ["João", "Maria", "José"]
notas = [8.5, 9, 6.5]
plt.bar(x=estudantes, height=notas)
plt.show()
'''

from random import choice

estudantes_2 = ["João", "Maria", "José", "Ana"]
print(choice(estudantes_2))
help(choice)

"""
A importação de métodos específicos de uma biblioteca pode trazer algumas vantagens para o nosso projeto como:

 * Economia de memória: quando importamos uma biblioteca inteira, todo o seu código é carregado na memória, mesmo que não 
                     utilizemos todos os seus métodos. Importar apenas os métodos que precisamos pode economizar memória, especialmente em programas com grandes bibliotecas.
 * Maior clareza no código: importar apenas os métodos que vamos usar torna o código mais claro e fácil de entender.
 * Redução de conflitos de nome: quando importamos uma biblioteca inteira, podemos acabar tendo conflitos de nome com outras variáveis ou funções em nosso código.
 * Redução no tempo de execução: como a biblioteca inteira não é importada, o tempo de execução do programa pode ser mais rápido, uma vez que menos código precisa ser carregado na memória e interpretado pelo interpretador Python.

Além das formas vistas anteriormente, podemos citar mais dois exemplos que você poderá encontrar ao longo de suas práticas e estudos da linguagem Python: from nome_biblioteca import met_1, met_2
Este código resulta na importação de 2 ou mais métodos de uma biblioteca, não necessitando repetir a importação desta a cada método desejado. Podemos, 
por exemplo, importar 2 métodos da biblioteca random para colher uma amostra de 5 valores de uma lista de 20 valores gerada aleatoriamente com números de 0 a 99.
"""

from random import randrange, sample
#Adiciono aleatoriamente 20 numeros entre 0 e 999
#randrange é semelhante ao choice, mas retorna apenas um elemento dentro do valor informado
lista = []

for number in range(0, 100):
    lista.append(randrange(1000))

nova_lista = sample(lista, 5)
print(nova_lista)

print()

import math

n = int(input("Digite um número positivo para calcular sua raiz quadrada:"))
print(f"\nA raiz quadrada de {n} é igual a {math.sqrt(n)}")

print()

from math import *

n = int(input("Digite um número positivo para calcular sua raiz quadrada:"))
print(f"\nA raiz quadrada de {n} é igual a {sqrt(n)}")

"""
Atenção: A importação nesse sentido precisa de alguns cuidados:

    * Podemos ter choque de nomes entre as variáveis. Por exemplo, no caso de termos uma função chamada sqrt antes de importar a da biblioteca math.
    * Podemos reduzir a eficiência da execução, se o número de funções importadas é grande.
    * Não fica explícito de onde aquela variável, método ou classe veio.

"""