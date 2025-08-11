import sqlite3


class DbOperations:
    def __init__(self):
        self.connection = sqlite3.connect("teams_db.db")
        self.cursor = self.connection.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.connection.close()

    def get_clubes(self):
        self.cursor.execute("SELECT * FROM equipas")
        return self.cursor.fetchall()

    def get_clube(self, campo, valor):
        self.cursor.execute(f"SELECT * FROM equipas WHERE {campo} = ?", (valor,))
        return self.cursor.fetchall()
