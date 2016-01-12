__author__ = 'Rafael'

# Inserindo e atualizando dados no banco de dados.
# Importando a biblioteca de banco de dados.
import sqlite3
# Criando a conexão como banco de dados.
db = sqlite3.connect('app27SupportFile.db')
# Criando uma tabela.
db.execute('CREATE TABLE person (firstname text, lastname text, age int)')
# Inserindo dados na tabela criada.
db.execute('INSERT INTO person (firstname, lastname, age) VALUES ("Rafael", "Marques", 32)')
# Fazendo o commit das instruções.
db.commit()
# Inserindo mais dados.
db.execute('INSERT INTO person (firstname, lastname, age) VALUES ("Andrei", "Marques", 25)')
# Fazendo o commit.
db.commit()
# Alterando dados já inseridos no banco de dados.
db.execute('UPDATE person SET firstname = "André" WHERE age = 25')
# Fazendo o commit.
db.commit()
# Inserindo último registro.
db.execute('INSERT INTO person (firstname, lastname, age) VALUES ("Daniel", "Marques", 32)')
# Fazendo o commit.
db.commit()