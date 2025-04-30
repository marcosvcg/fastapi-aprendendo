from repo import user_repo
from util.database import get_connection
from util.hasher import hash_password
from datetime import datetime

class UserService:
    def __init__(self):
        self.user_repo = user_repo

    def create_user(self, username: str, password: str):
        with get_connection() as conn:
            if self.user_repo.search_by_username(conn, username):
                raise ValueError("Username already registered.")

            hashed = hash_password(password)
            date_created = datetime.now()
            self.user_repo.save_user(conn, username, hashed, date_created)

    def delete_user(self, user_id: int):
        with get_connection() as conn:
            user = self.user_repo.search_by_id(conn, user_id)
            if not user:
                raise ValueError(f"User with id {user_id} not found")
            self.user_repo.delete_user(conn, user_id)
            return self.serialize_user_dict(user)

    def get_all_users(self) -> dict:
        with get_connection() as conn:
            return self.user_repo.search_all_users(conn)

    def get_user_by_id(self, user_id: int) -> dict:
        with get_connection() as conn:
            user = self.user_repo.search_by_id(conn, user_id)
            if not user:
                raise ValueError(f"User with id {user_id} not found")
            return self.serialize_user_dict(user)

    def get_user_by_username(self, username: str) -> dict:
        with get_connection() as conn:
            user = self.user_repo.search_by_username(conn, username)
            if not user:
                raise ValueError("User not found")
            return self.serialize_user_dict(user)

    def serialize_user_dict(self, user: dict) -> dict:
        return {
            "id": user["id"],
            "username": user["username"],
            "date_created": user["date_created"],
        }