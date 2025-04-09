from repo import user_repo
from util.database import get_conn
from util.hasher import hash_password

def create_user(username: str, password: str):
    conn = get_conn()

    if user_repo.search_by_username(conn, username):
        raise ValueError("Username already registered.")
    
    hashed = hash_password(password)
    user_repo.save_user(conn, username, hashed)


def get_all_users() -> dict:
    conn = get_conn()
    return user_repo.search_all_users(conn)

def get_user_by_id(user_id: int) -> dict:
    conn = get_conn()
    user = user_repo.search_by_id(conn, user_id)

    if not user:
        raise ValueError("User not found")

    return {
        "id": user["id"],
        "username": user["username"],
        # "hashed_password": user["hashed_password"]
    }