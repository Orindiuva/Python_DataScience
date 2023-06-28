import numpy as np
import matplotlib.pyplot as plt

dataset = np.loadtxt("apples_ts.csv", delimiter=",", usecols=range(1, 88, 1))

dados_transposto = dataset.T

#Cria um array com tamanho de 1 a 87
datas = np.arange(1, 88, 1)

precos = dados_transposto[:,1:6]

Moscow = precos[:,0]
#print(Moscow.shape)
plt.plot(datas, Moscow)
plt.show()

#Separando o array de MOsco por ano
Moscow_ano1 = Moscow[0:12]
Moscow_ano2 = Moscow[13:25]
Moscow_ano3 = Moscow[25:37]
Moscow_ano4 = Moscow[37:49]

plt.plot(range(1, 13, 1), Moscow_ano1)
plt.plot(range(1, 13, 1), Moscow_ano2)
plt.plot(range(1, 13, 1), Moscow_ano3)
plt.plot(range(1, 13, 1), Moscow_ano4)
plt.legend(['ano1', 'ano2', 'ano3', 'ano4'])
plt.show()

#Comparando arrays - comparado o preço da maça entre dois anos
result = np.array_equal(Moscow_ano3, Moscow_ano4)
print(result)
#Verifica se os valores entre as datas são semelhantes - verifica se os arrays são próximos (dentro de um intervalo).
#O últmo parametro indica a distância entre os arrays
print(np.allclose(Moscow_ano3, Moscow_ano4, 0.15))
print(np.allclose(Moscow_ano2, Moscow_ano4, 0.33))