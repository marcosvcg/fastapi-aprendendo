from fastapi import APIRouter, HTTPException
from service import user_service
from model.user import UserIn, UserOut

router = APIRouter()
service = user_service.UserService()

@router.get("/users")
def get_all_users():
    try:
        return service.get_all_users()
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.post("/user")
def create_user(user: UserIn):
    try:
        service.create_user(user.username, user.password)
        return {"message": "User registered successfully."}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/user/{id}")
def delete_user(id: int):
    try:
        service.delete_user(id)
        return {"message": "User deleted sucessfully."}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/user/id/{id}", response_model=UserOut)
def get_user_by_id(id: int):
    try:
        return service.get_user_by_id(id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/user/username/{username}", response_model=UserOut)
def get_user_by_username(username: str):
    try:
        return service.get_user_by_username(username)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))