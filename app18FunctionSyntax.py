__author__ = 'rafael'

# Apresentação de sintaxe de uma função. Iniciamos com a palavra reservada 'def' seguida do nome da função.
# Entre os parenteses pode haver parâmetros, mas são opcionais. Segue o exemplo.
# def function_name(param1,param2):
#     some code here

# Código de exemplo prático.

# Variáveis usadas.
list1 = [1,2,3,4]
list2 = [5,6,7,8]

# Funções.

# Exibe o conteúdo de uma lista. Passamos como parâmetro a lista.
def exibe_lista(list):
    print(list)

# Adiciona valores a uma lista. Passamos como parâmetros a lista e o valor.
def aumenta_lista(list, value):
    list.append(value)

# Removendo valores de uma lista. Passamos como parâmetros a lista e o valor.
def diminui_lista(list, value):
    list.remove(value)


# Testes.

# Testando função exibe_lista.
exibe_lista("Essa é a lista 1 original: {}".format(list1))
exibe_lista("Essa é a lista 2 original: {}".format(list2))

# Testando função aumenta_lista.
aumenta_lista(list1,5)
exibe_lista("Essa é a lista 1 depois da função 'aumenta_lista': {}".format(list1))

# Testando função diminui_lista
diminui_lista(list2,5)
exibe_lista("Essa é a lista 2 depois da função 'diminui_lista': {}".format(list2))
