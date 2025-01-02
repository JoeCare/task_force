from fastapi import APIRouter, HTTPException
from app.schemas import UserCreate, UserResponse, UserLogin
from tests.user_mock import UserMock, UserServiceMock
from app.utils.security import hash_password, verify_password


router = APIRouter()
user_service = UserServiceMock()

@router.post("/login")
def login(user: UserLogin):
    """Authenticates a user with their credentials."""
    users = user_service.get_all_users()
    user_db = next((u for u in users if u["email"] == user.email), None)
    if not user_db:
        raise HTTPException(status_code=400, detail="Invalid email or password.")
    if not verify_password(user.password, user_db["hashed_password"]):
        raise HTTPException(status_code=400, detail="Invalid email or password.")
    return {"message": "Login succesful", "user": UserResponse(**user_db)}

@router.get("/", response_model=list[UserResponse])
def read_users():
    return user_service.get_all_users()

@router.get("/{user_id}", response_model=UserResponse)
def read_user(user_id: int):
    user = user_service.get_user_by_id(user_id)
    if not user:
        return ("User not found in database.")
    return user

@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate):
    for user_db in user_service.get_all_users():
        if user_db["email"] == user.email:
            return "User already exixts!"
    hashed_password = hash_password(user.password)
    return user_service.create_user(user.username, user.email, hashed_password)
#TODO: debug this 

# httpx --method get http://127.0.0.1:8000/users/
# httpx --method POST http://127.0.0.1:8000/users/ --json '{"username": "testuser", "email": "test@example.pl", "password": "123secure"}'
# httpx --method POST http://127.0.0.1:8000/login --json '{"email": "johndoe@example.com", "password": "password123"}'
