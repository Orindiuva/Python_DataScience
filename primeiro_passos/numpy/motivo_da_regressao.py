import numpy as np
import matplotlib.pyplot as plt


dataset = np.loadtxt("apples_ts.csv", delimiter=",", usecols=range(1, 88, 1))

dado_transposto = dataset.T

precos = dado_transposto[:,1:6]

#Cria um array com tamanho de 1 a 87
datas = np.arange(1, 88, 1)

Moscow = precos[:,0]

Y = Moscow
X = datas
n = np.size(Moscow)

a = (n*np.sum(X*Y) - np.sum(X)*np.sum(Y))/(n*np.sum(X**2) - np.sum(X)**2)
print("Coeficiente angular:", a)

b = np.mean(Y) - a*np.mean(X)
print("Coeficiente linear: ", b)
y = a*X+b

plt.plot(datas, Moscow)
plt.plot(datas, y)
plt.show()


"""
Temos os valores dessa reta na posição dos meses, de 0 a 80, pulando a cada 20. Mas e se quisermos calcular o preço, 
conforme a equação da reta, na metade do mês, como em 41.5?

Para isso, basta utilizarmos a equação da reta com os coeficientes calculados. Ou seja, por termos ajustado os coeficientes, 
conseguimos calcular valores intermediários mesmo que eles não estejam no array, nos permitindo fazer uma estimativa de valor.

Podemos utilizar plt.plot() passando para a posição x o valor da posição que queremos calcular, e o cálculo de y. 
Adicionaremos, ainda, um terceiro parâmetro '*r' que deve demarcar com o asterisco o ponto do gráfico que estamos analisando.

"""

plt.plot(datas,Moscow)
plt.plot(X,y)
plt.plot(41.5,41.5*a+b,'*r')
plt.show()


"""
Não temos valores do mês 100, por exemplo, mas tendo o "a" e o "b" sabemos a taxa de crescimento e podemos ter uma estimativa do preço daqui a alguns meses.

Para isso, basta reproduzirmos o cálculo anterior alterando o mês:

"""

plt.plot(datas,Moscow)
plt.plot(X,y)
plt.plot(41.5,41.5*a+b)
plt.plot(100,100*a+b,'*r')
plt.show()

"""
Agora, além da marcação do mês 41.5, temos uma marcação de estimativa do valor para o mês 100, que atinge por volta de 123.
"""