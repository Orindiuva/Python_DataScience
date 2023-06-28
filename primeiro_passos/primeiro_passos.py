#Quantidade total de empregados
#O menor e o maior salário
#A média ponderada da faixa salarial da escola
import pandas

q_seguranca = 5
s_seguranca = 3000

q_docente = 16
s_docente = 6000

q_diretoria = 1
s_diretoria = 12500

lista_salario = [s_seguranca, s_docente, s_diretoria]
empregados = [q_seguranca, q_docente, q_diretoria]
total_empregados = sum(empregados)
print("Total de empregados  {}".format(total_empregados))
salario_mais_baixo = min(lista_salario)
salario_mais_alto = max(lista_salario)
print("Salario mais baixo: {}. Salario mais alto {}.".format(salario_mais_baixo, salario_mais_alto))


media_salarial = sum(lista_salario)/total_empregados
print("Media salarial: {:.2f}".format(media_salarial))
#A média ponderada é usada quando os valores individuais têm importâncias diferentes
media_ponderada_salarial = (s_seguranca*q_seguranca + s_docente*q_docente + s_diretoria*q_diretoria)/(total_empregados)
print("Média ponderada salários {:.2f}".format(media_ponderada_salarial))
