import numpy as np

#Gera 100 numeros aleatórios entre 40 e 100
numeros = np.random.randint(low=40, high=100, size=100)
#print(numeros, np.size(numeros))
#print()
"""
Nosso coeficiente angular é um número com vírgulas, então precisamos gerar um número do tipo float. 
Para isso, usamos a função random.uniform(), que gera valores aleatórios do tipo float.

Obs: utilizo o seed abaixo, caso tenha outro gerador de número aleatório essa seguência não utilizará esse seed, pois ele é reinicializado após a sua utilização. 
Esta função também recebe os parâmetros low, high e size:
"""
np.random.seed(16)
coef_angulares = np.random.uniform(low=0.10, high=0.90,size=100)
print(coef_angulares)

"""
Com os coeficientes angulares armazenados na variável, calcularemos o valor da norma para cada um deles. Ou seja, testaremos cada um.
Para isso, usaremos um loop for que deve percorrer por esses coeficientes e verificar a diferença entre 
o array de Moscow e o array calculado com o coeficiente de teste. Para essa verificação, usaremos linalg.norm(), que deve calcular o valor de y para cada iteração:

"""

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

b = np.mean(Y) - a*np.mean(X)

print("Calculando o coeficiente de teste ")

norma = np.array([])
for i in range(100):
    norma = np.append(norma, np.linalg.norm(Moscow-(coef_angulares[i]*X+b)))

min = norma.min()


for k, v in enumerate(norma):
    if min == v:
        print("Está na posição: {} com o valor de {}".format(k, v))
        print("Valor do coeficiente: ", coef_angulares[k])

"Salvando os valores de coeficiente angular dos valores normalizados"
dados = np.column_stack([norma, coef_angulares])
#np.savetxt(sys.stdout, my_array, '%19.2f')
dataset = np.loadtxt("dados.csv", delimiter=",")
print(dataset[56])