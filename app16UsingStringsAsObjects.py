__author__ = 'rafael'

# Strings podem ser trabalhadas de diferentes maneiras, como veremos.
# Declarando uma lista.
string = ['s','t','r','i','n','g']
# Exibindo os dados da lista
for letter in string:
    print(letter)

# Linha em branco para melhorar a leitura.
print()

# Mas podemos obter o mesmo resultado com uma variável do tipo String.
string2 = 'string'
# Exibindo da mesma forma que a lista.
for letter in string2:
    print(letter)

# Linha em branco para melhorar a leitura.
print()

# Algumas outras funções com Strings.
string3 = "This is a string of text, in a variable called string"
# Função que podemos usar para contar quantas vezes a letra 's' aparece dentro da string, por exemplo.
print(string3.count('s'))
# Podemos usar a função 'title' para tornar maiúscula a primeira letra de cada palavra na string.
print(string3.title())
# Existe uma função parecida, 'capitalize', mas que torna apenas a primeira letra da string inteira maiúscula.
string4 = "brasil"
print(string4.capitalize())