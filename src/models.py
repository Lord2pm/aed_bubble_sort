import mysql.connector as mysql


class Model():
	def __init__(self):
		self.connection = mysql.connect(user='root', host='127.0.0.1', password='', database='aed_bubble_sort')
		self.cursor = self.connection.cursor()

	def set_clube(self, nome, orcamento, qtd_titulos, logo):
		self.cursor.execute(f'INSERT INTO clubes (nome, orcamento, qtd_titulos, logo) VALUES ("{nome}", {orcamento}, {qtd_titulos}, "{logo}")')
		self.connection.commit()

	def get_clubes(self):
		self.cursor.execute('SELECT * FROM clubes')
		dados = self.cursor.fetchall()

		return dados

	def get_clube(self, campo, valor):
		self.cursor.execute(f'SELECT * FROM clubes WHERE {campo} = "{valor}"')
		dados = self.cursor.fetchall()

		return dados

	def update_clube(self):
		self.cursor.execute('UPDATE clubes SET orcamento = 58100000 WHERE id = 25')
		self.connection.commit()

	def close_database(self):
		self.connection.close()