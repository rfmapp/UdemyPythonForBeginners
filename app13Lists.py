__author__ = 'rafael'

# Listas.
# Variável.
list = [1,2,3,4,5,6,7,8,9,10,11]
# Exibindo todos os elementos.
print(list)
# Exibindo um elemento específico. O número se refere ao ídice do elemento.
print(list[4])
# Exibindo o tamanho da lista (quantidade de elementos).
print(len(list))
# Exibindo um intervalo de elementos. O valor final do intervalo deve ser lido como 'final -1'.
print(list[2:4])
# Modificando a lista.
list.append(12)
# Exibindo novamente todos os elementos da lista.
print(list)
# Criando uma nova lista.
list2 = [13,14,15]
# Adicionando os elementos da lista 2 na primeira lista.
list.extend(list2)
# Exibindo a primeira lista.
print(list)
# Podemos ainda inserir um novo item em um índice específico. Por exemplo, vamos adicionar um novo valor.
list.append(17)
# Exibindo a lista
print(list)
# Agora vamos corrigir a sequência adicionando o valor no local correto. Primeiro definimos o índice em que queremos
# inserir e depois o valor a ser inserido.
list.insert(15,16)
# Exibindo a lista.
print(list)
# Se o objetivo for alterar um valor, deve-se especificar o índice do valor a ser alterado e atribuir o novo valor.
list[16] = 18
# Exibindo a lista
print(list)