from fastapi import APIRouter, HTTPException
from service import user_service
from model.user import UserIn, UserOut

router = APIRouter()

@router.get("/users")
def get_all_users():
    try:
        return user_service.get_all_users()
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.post("/user")
def create_user(user: UserIn):
    try:
        user_service.create_user(user.username, user.password)
        return {"message": "User registered successfully."}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/user/{id}", response_model= UserOut)
def get_user(id: int):
    try:
        return user_service.get_user_by_id(id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))