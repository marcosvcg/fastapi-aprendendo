import sqlite3

conn = sqlite3.connect(':memory:', check_same_thread=False)
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        hashed_password TEXT NOT NULL,
        date_created TEXT NOT NULL
    )
''')
conn.commit()

# Função para acessar a conexão (ela é global, precisando ser acessada modularmente)
def get_conn():
    return conn