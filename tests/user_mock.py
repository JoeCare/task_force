from typing import TypedDict

class UserMock(TypedDict):
    id: int
    username: str
    email: str
    hashed_password: str
    is_active: bool

mock_users = [
    UserMock(id=1, username="testuser1", email="test1@example.pl", is_active=True),
    UserMock(id=2, username="testuser2", email="test2@example.pl", is_active=True),
    UserMock(id=3, username="testuser3", email="test3@example.pl", is_active=False)
]

class UserServiceMock:

    @staticmethod
    def get_user_by_id(user_id: int):
        for user in mock_users:
            if user.id == user_id:
                return user
        return None
    
    @staticmethod
    def get_all_users():
        return mock_users
    
    @staticmethod
    def create_user(username: str, email: str, hashed_password: str, is_active: bool = True):
        new_user = {
            "id": len(mock_users) + 1,
            "username": username,
            "email": email,
            "hashed_password": hashed_password,
            "is_active": is_active  #TODO: add functionality to activate user after changing the password with first login
        }
        mock_users.append(new_user)
        return new_user