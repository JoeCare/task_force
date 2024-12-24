from fastapi import APIRouter

router = APIRouter()

users_mock = [{"id": 1, "username": "Rick"}, {"id": 2, "username": "Morty"}]

@router.get("/")
def read_users():
    return users_mock

@router.get("/{user_id}")
def read_user(user_id: int):
    return users_mock[user_id - 1]