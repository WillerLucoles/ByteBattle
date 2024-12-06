import sqlite3
from datetime import datetime


class DBProxy:
    def __init__(self, db_name="scores.db"):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        """Cria a tabela de scores, se não existir."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS scores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                player TEXT NOT NULL,
                score INTEGER NOT NULL,
                date TEXT NOT NULL
            )
        """)
        self.connection.commit()

    def add_score(self, player, score):
        """Adiciona um novo score ao banco de dados."""
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.cursor.execute("INSERT INTO scores (player, score, date) VALUES (?, ?, ?)", (player, score, now))
        self.connection.commit()

    def get_scores(self):
        """Retorna todos os scores, ordenados por pontuação (decrescente)."""
        self.cursor.execute("SELECT player, score, date FROM scores ORDER BY score DESC LIMIT 10")
        return self.cursor.fetchall()

    def clear_scores(self):
        """Remove todos os scores (apenas para testes)."""
        self.cursor.execute("DELETE FROM scores")
        self.connection.commit()


    def close(self):
        """Fecha a conexão com o banco de dados."""
        self.connection.close()

