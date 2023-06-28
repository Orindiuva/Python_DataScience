"""
O formato mais simples desta função é o seguinte:
 * lambda <variavel>: <empressao>

 Situação: Nesta nova demanda, precisamos criar uma calculadora simples da média ponderada de notas de uma dada matéria.
  Vamos requisitar ao usuário a entrada das 3 notas (N1, N2, N3) do estudante e devolver a média ponderada deste estudante.
  Os pesos das notas são de, respectivamente 3, 2, 5.
  Precisamos exibir um pequeno texto em que indicamos a média do(a) estudante. Vamos resolver esse desafio?
"""

# Recebendo as notas e calculando a média ponderável

#N1 = float(input("Digite a 1ª nota do(a) estudante: "))
#N2 = float(input("Digite a 2ª nota do(a) estudante: "))
#N3 = float(input("Digite a 3ª nota do(a) estudante: "))

#media_ponderada = lambda x, y, z: (N1*3 + N2*2 + N3*5)/10

#media_estudante = media_ponderada(N1, N2, N3)
# Exibindo a média
#print(f'O(a) estudante atingiu uma média de {media_estudante}')


"""
Situação: Recebemos mais uma demanda, desta vez, para criar uma pequena função que pudesse adicionar qualitativo 
(pontuação extra) às notas do trimestre dos estudantes da turma que ganhou a gincana de programação promovida pela escola. 
Cada estudante receberá o qualitativo de 0.5 acrescido à média. Os dados recebidos correspondem a uma lista contendo as 
notas de alguns estudantes e uma variável com o qualitativo recebido.]]]
"""

# Notas do(a) estudante
notas =  [6.0, 7.0, 9.0, 5.5, 8.0]
qualitativo = 0.5

notas_atualizadas = map(lambda x: x + qualitativo, notas)

print(type(notas_atualizadas))
for i in notas_atualizadas:
    print(i)

print("xxxxxxxxxxxxx - Celsius to Fahrenheit - xxxxxxxxxxxxxxx")
temp_celsius = [0, 25, 37, 78, 100]
#formula
#temp_fahrenheit = temp_celsius * 9/5 + 32
temp_fahrenheit = list(map(lambda temperatura: (temperatura * 9/5 + 32), temp_celsius))
#print(f"Temperatura fahrenheit {list(temp_fahrenheit)}")
lista_temperatura = []
#lista_temperatura.append(temp_celsius)
#lista_temperatura.append(temp_fahrenheit)
for index, celsius in enumerate(temp_celsius):
    print(f"Temperatura Celsius: {temp_celsius[index]} - Fahrenheit {int(temp_fahrenheit[index])}")

