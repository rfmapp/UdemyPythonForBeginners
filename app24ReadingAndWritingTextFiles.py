__author__ = 'Rafael'

# Recaptulando, vamos ler o conteúdo de um arquivo existente.
input = open('app23SupportFile.txt', 'r')
# Exibindo o contéudo do arquivo.
for line in input:
    print(line, end = '')

# Abrindo um arquivo para escrita de dados. Se o arquivo não existir, será criado.
output = open('app24SupportFile.txt', 'w')
# Podemos usar a leitura do arquivo anterior para escrever os mesmos dados no novo arquivo.
for line in input:
    print(line, file = output, end = '')