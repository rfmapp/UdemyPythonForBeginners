__author__ = 'Rafael'

# Inserindo e atualizando dados no banco de dados.
# Importando a biblioteca de banco de dados.
import sqlite3
# Criando a conexão como banco de dados.
db = sqlite3.connect('app27SupportFile.db')
# Executando query para recuperar dados de uma tabela. Utilizaremos o banco de dados da aula anterior.
# Jogaremos o resultado em uma variável.
result = db.execute('SELECT * FROM person')
# Faremos um loop para exibir os dados obtidos.
for each in result:
    print(each)

# Podemos tratar os dados obtidos como um dicionário, fazendo apenas algumas alterações.
db.row_factory = sqlite3.Row
# Jogaremos o resultado em uma nova variável, para deixa clara a diferença.
result2 = db.execute('SELECT * FROM person')
# Repetimos o loop, agora especificando o dicionário
for each in result2:
    print(dict(each))

# Vamos agora inserir um registro para depois mostrar como exclui-lo.
db.execute('INSERT INTO person (firstname, lastname, age) VALUES ("Daoido", "Maluco", 100)')
# Commit
db.commit()
# Agora excluímos o registro.
db.execute('DELETE FROM person WHERE lastname = "Maluco"')
# Commit
db.commit()