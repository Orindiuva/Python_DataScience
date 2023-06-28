#Notas do(a) estudante
notas = {'19 Trimestre': 8.5, '2° Trimestre': 9.5, '3º trimestre': 7}


# Calculando a soma
soma = 0

for nota in notas.values():
    soma += nota
print(soma)
print(sum(notas.values()))


def soma(nota1, nota2, nota3):
    print("nota1:", nota1)
    print("nota2:", nota2)
    print("nota3:", nota3)

nota1 = 10
nota2 = 20
nota3 = 30
print()
soma(nota1, nota2, nota3)
print()
soma(nota3, nota2, nota1)
print("Parametros nomeados")
soma(nota3=nota3, nota2=nota2, nota1=nota1)


# Notas do(a) estudante
notas = [6.0, 7.0, 9.0, 5.0]

def boletim(lista):
    media = sum(lista) / len(lista)

    if media >= 6:
        situacao = "Aprovado(a)"
    else:
        situacao = "Reprovado(a)"

    #return (media, situacao)
    return media, situacao

print(boletim(notas))
nota, situacao = boletim(notas)
print(nota)
print(situacao)