__author__ = 'rafael'

# Lidando com erros e excessões (tratamento de erros).
tuple = (1,2,3,4,5)
try:
    tuple.append(6)
    for each in tuple:
        print(each)
except AttributeError as error:
    print("Error formed: ", error) # Excessão lançada para informar o erro. Fica mais interessante a exibição dos erros.