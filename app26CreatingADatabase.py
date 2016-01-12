__author__ = 'Rafael'

# Demonstração de como trabalhar com banco de dados.
# Importação da biblioteca do banco de dados Sqlite3
import sqlite3
# Criação do objeto com a conexão com o banco de dados.
db = sqlite3.connect('app26SupportFile.db')
# Criando uma tabela. Passagem de uma query.
db.execute('CREATE TABLE person (firstname text, lastname text, age int)')