from fastapi import APIRouter, HTTPException
from app.schemas import UserCreate, UserResponse
from tests.user_mock import UserMock, UserServiceMock

router = APIRouter()
user_service = UserServiceMock()


@router.get("/", response_model=list[UserResponse])
def read_users():
    return user_service.get_all_users()

@router.get("/{user_id}")
def read_user(user_id: int):
    user = user_service.get_user_by_id(user_id)
    if not user:
        raise HTTPException(404, "User not found in database.")
    return user