__author__ = 'Rafael'

# Demonstra como lidar com erros de tempo de execução.

#Variáveis.
first = 4
second = 5
third = 2
more = input("What is the extra value?") # O primeiro problema está aqui, o valor da variável precisa ser 'transformado' em um inteiro, pois será parte de uma operação aritmética.
# more = int(input("What is the extra value?"))
total = first+seocnd+third+more # O segundo problema está aqui, um erro na escrita de uma das variáveis.

# Exibição do resultado.
print(total)

# O erro não interrompe a execução do programa, é exibido ao final da execução apenas.