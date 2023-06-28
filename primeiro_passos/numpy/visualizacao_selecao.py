import numpy as np
import matplotlib.pyplot as plt

dataset = np.loadtxt("apples_ts.csv", delimiter=",", usecols=range(1, 88, 1))

dados_transposto = dataset.T
#Pega todas as linhas da primeira coluna
datas = dados_transposto[:,0]
print(datas)
#Cria um array com tamanho de 1 a 87
datas = np.arange(1, 88, 1)

#Pega todoas as linhas, e colunas de 1 a 6, excluido da seleção a primeira coluna (que contem as datas (mes.ano)
precos = dados_transposto[:,1:6]




#plt.plot(precos)
#Precos da primeira cidade Moscow
plt.plot(datas, precos[:,0])
plt.title("Cidades")
plt.show()

#Precos das cidade Moscow e Kaliningrad
#plt.plot(datas, precos[:,0:2])
#plt.show()

Moscow = precos[:,0]
Kaliningrad = precos[:,1]
Petersburg = precos[:,2]
Krasnodar = precos[:,3]
Ekaterinburg = precos[:,4]

