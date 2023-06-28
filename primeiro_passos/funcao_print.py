

print("xxxxxx - f-string (ou formatação de string) - xxxxxx")
nome = "Ana Maria"
idade = 17
print(f"O nome da aluna é {nome} e sua idade é {idade} anos.")
print()
print("xxxxx - Operador de formatação - xxxxxx")
'''
Tipo de variável	Palavra-chave
string           	%s
inteiro	            %d
float	            %f
caractere	        %c
'''

nome_aluno = 'Fabricio Daniel'
print('Nome do aluno: %s' %(nome_aluno))

nome_aluno = 'Fabricio Daniel'
idade_aluno = 15
media_aluno = 8.45

print('Nome do aluno é %s, ele tem %d anos e sua média é %f.' %(nome_aluno, idade_aluno, media_aluno))
print('Nome do aluno é %s, ele tem %d anos e sua média é %.2f.' %(nome_aluno, idade_aluno, media_aluno))

x = True
print("Valor de x: %s" % str(x))
print()

print("xxxxx - Format - xxxxxx")

nome_aluno = 'Fabricio Daniel'
print('Nome do aluno: {}'.format(nome_aluno))

nome_aluno = 'Fabricio Daniel'
idade_aluno = 15
media_aluno = 8.45
print('Nome do aluno é {}, ele tem {} anos e sua média é {}.' .format(nome_aluno, idade_aluno, media_aluno))
print()

print("xxxxx - Caracteres especiais - xxxxxx")
print("Estudar é um esforço constante,\nÉ como cultivar uma planta,\nPrecisamos de dedicação e paciência,\nPara ver o fruto amadurecer.")
print()
print('Quantidade\tQualidade\n5 amostras\tAlta\n3 amostras\tBaixa')
print()
print("Caminho do arquivo: C:\\arquivos\\documento.csv")
print("Ouvi uma vez \"Os frutos do conhecimento são os mais doces e duradouros de todos.\"")
print('Minha professora uma vez disse \'Estudar é a chave do sucesso.\' ')


nomes = "marcelo, katia, roberto"
print("marcelo" in nomes)
print("antonio" in nomes)