import bcrypt

def hash_password(password: str) -> str:
   # Gerar hash da senha para salvar usuario no banco de dados de forma segura
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')