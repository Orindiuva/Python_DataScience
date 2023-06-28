"""

No Python existem basicamente duas formas distintas de erros: os erros de sintaxe e as exceções. As exceções são uma
forma de lidar com erros e situações inesperadas no código, garantindo um fluxo de execução mais controlado.

E, como uma pessoa cientista de dados, você precisará ter atenção a situações como esta para evitar bugs ou problemas
em seus códigos e análises que possam afetar a experiência tanto da pessoa usuária quanto a eficiência da sua análise.

As exceções: são errros detectados durante a execução do programa. Elas interrompem
o fluxo do programa quando não tratadas.

Sintaxe Error:
Ocorre quando é detectado pelo parser (analisador) um erro na descrição do código. Normalmente uma seta aponta para
a parte do código que gerou o erro, como uma espécie de dica onde o erro possa ter ocorrido.
"""
#print(10 / 2

"""
NameError:
Exceção lançada quando tentamos utilizar um nome de algum elemento que não está presente em nosso código.
Neste caso, o interpretador não consegue aplicar o método da raiz quadrada por não ter sido importado junto a biblioteca math
"""
#raiz = sqrt(100)

"""
IndexError:
Exceção lançada quando tentamos indexar alguma estrutura de dados como lista, tupla ou até string além de seus limites.
"""

#lista = [1, 2, 3]
#lista[4]

"""
Type error
Exceção lançada quando um operador ou função são aplicados a um objeto cujo tipo é inapropriado.
"""
#i = 10
#ii = ""
#iii = i + ii

"""
KeyError:
Exceção lançada quando tentamos acessar uma chave que não está no dicionário presente em nosso código.
"""

#estados = {'Bahia': 1, 'São Paulo': 2, 'Goiás': 3}
#estados["Amazonas"]

"""
Warging:
Exceção lançada em situações que precisamos alertar ao usuário sobre algumas condições do código.

Essas condições não necessariamente interrompem a execução do programa, mas podem lançar avisos sobre uso de módulos 
obsoletos, ou que possam ser depreciados em atualizações futuras ou também para alterações que podem reverberar sobre alguma parte do código.

Lembrando que, no caso dos Warnings eles podem ser ignorados ou tratados como exceções.

"""

#a = np.arange(5)
#a / a  # apresenta um warning

#print("teste")

#div = 10/0

#print("teste1")

"""
Try...Except
Nela, temos dois tipos de cláusulas em que try representa o código padrão. Caso não ocorra nenhuma exceção, ele será executado por completo e o programa seguirá.

Se uma exceção for lançada, quebramos a execução de try e continuamos com o que precisa ser executado em except, que 
seria a cláusula de exceção. Ou seja, a cláusula except só será acionada se uma exceção for lançada na cláusula try.

Else
O else, semelhante à if...else, pega o caso contrário. Ou seja, se não tiver uma exceção, seguimos o fluxo do try e ao concluí-lo com sucesso saltamos para o else.

inally
O try corresponde ao fluxo normal, except ao fluxo de exceção, e else para o caso em que a exceção não for lançada. 
O finally, por sua vez, funciona para os casos em que qualquer uma das duas situações ocorra. Ou seja, tendo ou não exceção, a cláusula finally será executada.


"""

"""
Situação:
Você criou um código que lê um dicionário com as notas dos estudantes e quis retornar a lista de notas de determinado(a) 
estudante. Caso o(a) estudante não esteja matriculado(a) na turma, devemos tratar a exceção para aparecer a mensagem 
"Estudante não matriculado(a) na turma". Vamos trabalhar nesse exemplo com a exceção Key Error que interromperá o processo desse pedaço do código. Vamos testar esse primeiro tratamento?


notas = {'João': [8.0, 9.0, 10.0], 'Maria': [9.0, 7.0, 6.0], 'José': [3.4, 7.0, 8.0],'Cláudia': [5.5, 6.6, 8.0],
         'Ana': [6.0, 10.0, 9.5], 'Joaquim': [5.5, 7.5, 9.0], 'Júlia': [6.0, 8.0, 7.0], 'Pedro': [3.0, 4.0, 6.0]}

nome_estudante = input("Por favor informe o nome do(a) estudante:")

try:
    nota_estudante = notas[nome_estudante]
except KeyError as e:
    print(f"Estudante {nome_estudante} não matriculado(a) na turma")
else:
    print(f"Estudante {nome_estudante} possui a nota: {nota_estudante}")
finally:
    print("A consulta foi encerrada!")
"""

"""
Raise:

Outra forma de trabalhar com exceções, é criar uma própria pensando em um comportamento que não queremos que 
ocorra em nosso programa. Para isso, usamos a palavra-chave raise que permitirá que lancemos uma exceção.
"""
#raise ValueError("A lista de notas deve possuir dez elementos")


"""
Situação:
Você criou uma função para calcular a média de um estudante em uma dada matéria passando em uma lista as notas deste estudante. Você pretende tratar 2 situações:

 - Se a lista possuir um valor não numérico o cálculo de média não serà executado e uma mensagem de "Não foi possível calcular a média do(a) estudante. Só são aceitos valores numéricos!" será exibida.
 - Se a lista possuir um valor não numérico o cálculo de média não serà executado e uma mensagem de "Não foi possível calcular a média do(a) estudante. Só são aceitos valores numéricos!" será exibida.
"""
def media(lista: list=[0]) -> float:
    ''' Função para calcular a média de notas passadas por uma lista

    lista: list, default[0]
        Lista com as notas para calcular a média
        return calculo: float
        Média calculada
    '''

    calculo = sum(lista) / len(lista)

    if len(lista) > 4:
        raise ValueError("A lista não pode possuir mais de 4 notas.")


    return calculo



try:
    #notas = [6, 7, 8, "9"]
    #notas = [6, 7, 8, 9, "9"]
    notas = [6, 7, 8, 9, 9]
    #notas = [6, 7, 8, 9]
    resultado = media(notas)

except TypeError:
    print("Não foi possível calcular a média do(a) estudante. Só são aceitos valores numéricos!")
except ValueError as e:
    print(e)
else:
    print(resultado)
finally:
    print("A consulta foi encerrada!")
