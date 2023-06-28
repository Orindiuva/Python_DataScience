import numpy as np
import matplotlib.pyplot as plt

dataset = np.loadtxt("apples_ts.csv", delimiter=",", usecols=range(1, 88, 1))

dados_transposto = dataset.T

#Cria um array com tamanho de 1 a 87
datas = np.arange(1, 88, 1)

precos = dados_transposto[:,1:6]

Moscow = precos[:,0]
Kaliningrad  = precos[:,1]
print(Kaliningrad)
#Verificando a quantidade de NaNs no dataset
print("Total de valores nulos (NaNs): {}".format(sum(np.isnan(Kaliningrad))))
#Media dos valores anterios e posterior ao NaNs - media dos valores intermediarios
print("Média:", (Kaliningrad[3]+Kaliningrad[5])/2)
print("Mèdia:", np.mean([Kaliningrad[3],Kaliningrad[5]]))
Kaliningrad[4] = np.mean([Kaliningrad[3],Kaliningrad[5]])


#print(Moscow.shape)
plt.plot(datas, Kaliningrad )
plt.show()

#Separando o array de MOsco por ano
Kaliningrad_ano1 = Kaliningrad [0:12]
Kaliningrad_ano2 = Kaliningrad [13:25]
Kaliningrad_ano3 = Kaliningrad [25:37]
Kaliningrad_ano4 = Kaliningrad [37:49]

#Comparando a média de preços de duas cidades
print("Média do preço da maça em Moscow: {:.2f}".format(np.mean(Moscow)))
print("Média do preço da maça em Kaliningrad: {:.2f}".format(np.mean(Kaliningrad)))
