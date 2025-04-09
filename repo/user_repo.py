def save_user(conn, username: str, hashed_password: str):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, hashed_password) VALUES (?, ?)", (username, hashed_password))
    conn.commit()

def search_all_users(conn) -> dict:
    cursor = conn.cursor()
    cursor.execute("SELECT id, username FROM users ORDER BY id")
    rows = cursor.fetchall()
    return [{"id": row[0], "username": row[1]} for row in rows]

def search_by_username(conn, username: str) -> bool:
    cursor = conn.cursor()
    cursor.execute("SELECT 1 FROM users WHERE username = ? LIMIT 1", (username,))
    return cursor.fetchone() is not None

def search_by_id(conn, user_id: int) -> dict | None:
    cursor = conn.cursor()
    cursor.execute("SELECT id, username FROM users WHERE id = ?", (user_id,))
    row = cursor.fetchone()
    if row:
        return {
            "id": row[0],
            "username": row[1],
            # "hashed_password": row[2],
        }
    return None

