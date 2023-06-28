import numpy as np
import matplotlib.pyplot as plt

dataset = np.loadtxt("apples_ts.csv", delimiter=",", usecols=range(1, 88, 1))

dado_transposto = dataset.T

precos = dado_transposto[:,1:6]

#Cria um array com tamanho de 1 a 87
datas = np.arange(1, 88, 1)


Moscow = precos[:,0]
Kaliningrad = precos[:,1]
Petersburg = precos[:,2]
Krasnodar = precos[:,3]
Ekaterinburg = precos[:,4]


#Ajustar a reta para entender a taxa de crescimento do preço das maças.
#y-preço da maça
#a-coeficiente angular (o ângulo da reta
#b-coeficiente linear (onde a reta corta o eixo y (eixo das maças))
#x=mês
#y=ax+b - equação da reta
x = datas
y=2*x+80

plt.plot(datas, Moscow)
plt.plot(datas, y)
plt.show()

#Diferença da reta para os dados - uma métrica de quanto a reta se ajustou aos dados
#print(Moscow-y)
#Para retirar os valores negativos - função power eleva os valores a uma potência (quadrado)
#print(np.power(Moscow-y, 2))
#Aqui é o número que resume a qualidade do ajuste
soma_total_ajuste = np.sum(np.power(Moscow-y, 2))
print(np.sum(soma_total_ajuste))
#Retornando a raiz quadrada
print("Raiz quadrada:", np.sqrt(soma_total_ajuste))

#Tentando achar um ajuste melhor para a reta
y = 0.52 * x + 80
#print("valor de y:",y)
plt.plot(datas, Moscow)
plt.plot(datas, y)
plt.show()
soma_total_ajuste = np.sum(np.power(Moscow-y, 2))
print("Raiz quadrada:", np.sqrt(soma_total_ajuste))

#Essa funçãodo numpy faz realiza o calculo necessário:
valor_ajuste = np.linalg.norm(Moscow-y)
print("Linear log norm: ", valor_ajuste)

"""
Calculando o coeficiente angular (a)

A equação de uma reta na forma y = ax + b é uma expressão matemática que descreve a relação entre os valores de x e y em uma linha reta. 
O valor de "a" representa a inclinação (ou declive) da reta, que é a taxa de variação entre os valores de x e y. 
O valor de "b" é o ponto de intercepção no eixo y, ou seja, o valor de y quando x é igual a zero. 
Com essa equação, é possível plotar a reta em um sistema de coordenadas cartesianas, onde o eixo x representa os valores de x e o eixo y representa os valores de y.
A equação da reta é amplamente utilizada em várias áreas da matemática e também em outras áreas, como física e engenharia, para modelar dados e prever comportamentos futuros.
O coeficiente angular pode ser obtido pela seguinte equação: 

â = n * Soma(Xi * Yi) - Soma(Xi) * Soma(Yi)/(nSoma(X²i) - (Soma(Xi)²)

â = coeficiente angular;
n = número de elementos;
Y = Moscow;
X = datas.

"""

Y = Moscow
X = datas
n = np.size(Moscow)

a = (n*np.sum(X*Y) - np.sum(X)*np.sum(Y))/(n*np.sum(X**2) - np.sum(X)**2)
print("Coeficiente angular:", a)
y = a * x + 80
plt.plot(datas, Moscow)
plt.plot(datas, y)
plt.show()


"""
Calculando o coeficiente linear (b)

Para calcular o coeficiente linear, usamos a seguinte fórmula:
  b^= Media(Yi) - â * Media(Xi)
"""
b = np.mean(Y) - a*np.mean(X)
print("Coeficiente linear: ", b)
y = a*X+b

plt.plot(datas, Moscow)
plt.plot(datas, y)
plt.show()
""""
Lembre-se que o Y em maiúsculo corresponde aos valores de Moscow, e neste cálculo queremos o valor de y (minúsculo).
"""

valor_ajuste = np.linalg.norm(Moscow-y)
print("Linear log norm: ", valor_ajuste)