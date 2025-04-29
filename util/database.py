import sqlite3
from contextlib import contextmanager
from util.hasher import hash_password
from datetime import datetime

_conn = sqlite3.connect(':memory:', check_same_thread=False)
cursor = _conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        hashed_password TEXT NOT NULL,
        date_created TEXT NOT NULL
    )
''')
_conn.commit()

cursor.execute('''
    INSERT INTO users (username, hashed_password, date_created)
    VALUES (?, ?, ?)
''', ('red8732', hash_password('senha123'), datetime.now().isoformat()))

cursor.execute('''
    INSERT INTO users (username, hashed_password, date_created)
    VALUES (?, ?, ?)
''', ('a7x', hash_password('123456789'), datetime.now().isoformat()))

cursor.execute('''
    INSERT INTO users (username, hashed_password, date_created)
    VALUES (?, ?, ?)
''', ('slipknot', hash_password('abc'), datetime.now().isoformat()))

cursor.execute('''
    INSERT INTO users (username, hashed_password, date_created)
    VALUES (?, ?, ?)
''', ('s0ad_', hash_password('safepassword'), datetime.now().isoformat()))

_conn.commit()

# Função para acessar a conexão (ela é global, precisando ser acessada modularmente)
def get_conn():
    return _conn

# Gerenciar a abertura/fechamento da conexão nos métodos
@contextmanager
def get_connection():
    conn = get_conn()
    try:
        yield conn
    finally:
        pass # usar conn.close() apenas quando o banco não for em memória