__author__ = 'Rafael'

# Abre o arquivo para a leitura dos dados
file = open('app23SupportFile.txt')
# Faz a exibição do que está escrito em cada linha do arquivo.
for line in file:
    print(line, end = '')