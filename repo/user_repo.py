def save_user(conn, username: str, hashed_password: str, date_created: str):
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO users (username, hashed_password, date_created) VALUES (?, ?, ?)",
        (username, hashed_password, date_created)
    )
    conn.commit()

def search_all_users(conn) -> dict:
    cursor = conn.cursor()
    cursor.execute("SELECT id, username, date_created FROM users ORDER BY id")
    rows = cursor.fetchall()
    return [{"id": row[0], "username": row[1], "date_created": row[2]} for row in rows]

def search_by_username(conn, username: str) -> bool:
    cursor = conn.cursor()
    cursor.execute("SELECT id, username, date_created FROM users WHERE username = ? LIMIT 1", (username,))
    row = cursor.fetchone()
    if row:
        return {
            "id": row[0],
            "username": row[1],
            "date_created": row[2]
        }
    return None

def search_by_id(conn, user_id: int) -> dict | None:
    cursor = conn.cursor()
    cursor.execute("SELECT id, username, date_created FROM users WHERE id = ?", (user_id,))
    row = cursor.fetchone()
    if row:
        return {
            "id": row[0],
            "username": row[1],
            "date_created": row[2]
        }
    return None