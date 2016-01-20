__author__ = 'Rafael'

# Utilização de bibliotecas nativas.
# Importação das bibliotecas.
import datetime
import os

# Criação do objeto.
now = datetime.datetime.now()
# Exibe a data e hora atual.
print(now)

# Criando outro objeto.
my_os = os.name
# Exibe o sistema operacional.
print(my_os)
# Criando objeto.
user_os = os.getlogin()
# Exibe o usuário logado no sistema operacional.
print(user_os)